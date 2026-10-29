"""S46 follow-up: numerical checks of the statements added to the Hub.

    python3 -I check_followup.py      (exit code 1 if any check fails)

1. dual-currency-inflation 3.1/3.3 (B013): with B_spent + B_conv <= B_t + B_rec per
   household, and every unit received as payment spent by someone else, total
   conversions are at most N x B_t, even when received units are spent again.
2. dual-currency-inflation 3.4 (B013): total converted currency is at most
   (R x Q)_max x min(sum of capacities, N x B_t).
3. dual-currency-inflation 3.2 (B067): one capacity per person, the highest industry capacity.
4. integrated-digital-governance 4.3 (B108): one flow per pair of zones conserves
   population, and no one leaves an empty zone.
"""
import random

random.seed(46)
ok_all = []


def check(name, ok, detail):
    ok_all.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")


# 1-2. Basic units move between households over several rounds within a period.
B, N = 1200.0, 400
worst_ratio = 0.0
ceiling_ok = True
for trial in range(200):
    holding = [B] * N              # units each household can still use
    spent = [0.0] * N
    conv = [0.0] * N
    rec = [0.0] * N
    for _ in range(5):             # payments can be re-spent several times
        for i in range(N):
            if holding[i] <= 0:
                continue
            x = random.uniform(0, holding[i])
            if random.random() < 0.3:      # convert part of what is held
                conv[i] += x
            else:                          # spend it with another household
                j = random.randrange(N)
                spent[i] += x
                rec[j] += x
                holding[j] += x
            holding[i] -= x
    budget = all(spent[i] + conv[i] <= B + rec[i] + 1e-6 for i in range(N))
    worst_ratio = max(worst_ratio, sum(conv) / (N * B))
    ceiling_ok &= budget
    caps = [B * 2 ** min(random.randint(0, 7), random.randint(4, 8)) for _ in range(N)]
    rates = [random.uniform(1, 14) * random.uniform(0.5, 2.0) for _ in range(N)]
    converted = sum(min(c, e) * r for c, e, r in zip(caps, conv, rates))
    ceiling_ok &= converted <= max(rates) * min(sum(caps), N * B) + 1e-6
check("B013 budget and bound", ceiling_ok and worst_ratio <= 1 + 1e-12,
      f"every household within its budget; conversions at most {worst_ratio:.3f} x N x B_t over 200 trials")
check("B013 ceiling", ceiling_ok, "sum P_convert <= (R x Q)_max x min(sum C, N x B_t) in every trial")

# 3. Capacity across industries.
O_ij, O_bar = [3, 5, 1], [4, 4, 8]
C_ij = [B * 2 ** min(o, ob) for o, ob in zip(O_ij, O_bar)]
check("B067 capacity", max(C_ij) == B * 2 ** 4, f"industry capacities {C_ij}: capacity {max(C_ij):.0f}, not their sum {sum(C_ij):.0f}")

# 4. Zone flows.
K = 6
worst = 0.0
empty_ok = True
for _ in range(500):
    Z = [random.uniform(0, 1000) for _ in range(K)]
    Z[random.randrange(K)] = 0.0
    C = [random.uniform(300, 1500) for _ in range(K)]
    M = [[0 if i == j else random.uniform(0, 0.05) for j in range(K)] for i in range(K)]
    P = [random.uniform(0, 1) for _ in range(K)]
    F = [[0 if i == j else M[i][j] * Z[i] * (1 - abs(P[i] - P[j])) * (Z[i] / C[i]) for j in range(K)] for i in range(K)]
    dZ = [sum(F[i][k] for i in range(K)) - sum(F[k][j] for j in range(K)) for k in range(K)]
    worst = max(worst, abs(sum(dZ)))
    empty_ok &= all(sum(F[k]) == 0 for k in range(K) if Z[k] == 0)
check("B108 zone flows", worst < 1e-9 and empty_ok, f"largest |sum dZ_k/dt| {worst:.1e}; no outflow from an empty zone")

print(f"\n{sum(ok_all)} of {len(ok_all)} checks pass")
raise SystemExit(0 if all(ok_all) else 1)
