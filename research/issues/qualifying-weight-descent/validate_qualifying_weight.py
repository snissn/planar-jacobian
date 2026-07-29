#!/usr/bin/env python3
"""Entry point for exact issue #41 qualifying-weight regression checks."""
from qwd_search_core import *  # noqa: F401,F403
from qwd_search_symbolic import *  # noqa: F401,F403
from qwd_search_support import *  # noqa: F401,F403


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-weight", type=int, default=96)
    parser.add_argument("--max-n", type=int, default=10)
    parser.add_argument("--fan-instances", type=int, default=24)
    parser.add_argument("--support-degree", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_weight < max(16, args.max_n):
        raise SystemExit("--max-weight must be at least max(16,--max-n)")
    if not 3 <= args.support_degree <= 7:
        raise SystemExit("--support-degree must be between 3 and 7")
    campaign_affine_obstruction(args.max_weight, args.max_n)
    campaign_binomial_chain(min(args.max_n, 8))
    campaign_formal_23()
    campaign_finite_fan(args.max_weight, args.fan_instances)
    campaign_exhaustive_binomial_supports(args.support_degree)
    campaign_adjacent_edges()
    support_records = campaign_support_level(args.max_n, args.max_weight)
    payload = {
        "role": "research-worker",
        "issue": 41,
        "owned_path": "research/issues/qualifying-weight-descent/",
        "bounds": {
            "max_weight_coordinate": args.max_weight,
            "max_binomial_family_n": args.max_n,
            "fan_instances": args.fan_instances,
            "exhaustive_two_term_total_degree": args.support_degree,
        },
        "counts": asdict(COUNTS),
        "levels": {
            "support": "affine A_N local minima and exhaustive two-term support pairs",
            "formal_layer": "complete B_N systems, saturated (2,3), and surviving bounded two-term systems",
            "polynomial": "A_N and B_N witnesses are actual polynomials",
            "Keller": "witnesses have exact J=1 and explicit triangular inverses",
        },
        "support_records": support_records,
        "disposition": (
            "PASS: affine-only boundedness is falsified by actual Keller automorphisms; "
            "no resistant formal Keller pair survives the declared bounded library"
        ),
        "authority": "REGRESSION_AND_FALSIFICATION_EVIDENCE_ONLY",
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("qualifying-weight exact search: PASS")
        print(f"primitive weights: {COUNTS.primitive_weights}")
        print(f"affine A_N instances: {COUNTS.affine_family_instances}")
        print(f"affine weight evaluations: {COUNTS.affine_weight_evaluations}")
        print(f"finite-fan instances: {COUNTS.fan_instances}")
        print(f"finite-fan brute comparisons: {COUNTS.fan_bruteforce_comparisons}")
        print(f"binomial-chain instances: {COUNTS.binomial_chain_instances}")
        print(f"complete Jacobian equations: {COUNTS.binomial_chain_equations}")
        print(f"missing-support patterns: {COUNTS.missing_support_patterns}")
        print(f"saturated named formal ideals: {COUNTS.formal_ideals}")
        print(
            "exhaustive two-term support pairs: "
            f"{COUNTS.exhaustive_support_pairs} "
            f"(degree <= {args.support_degree})"
        )
        print(f"axis-admissible support pairs: {COUNTS.exhaustive_axis_admissible_pairs}")
        print(f"support pairs with exact minimum >=6: {COUNTS.exhaustive_high_defect_pairs}")
        print(f"face-compatible high-defect pairs: {COUNTS.exhaustive_face_compatible_pairs}")
        print(f"saturated bounded formal systems: {COUNTS.exhaustive_formal_systems}")
        print(f"bounded formal survivors: {COUNTS.exhaustive_formal_survivors}")
        print(f"adjacent nonzero-vertex solutions checked: {COUNTS.adjacent_edge_solutions}")
        print(f"mutation controls: {COUNTS.mutation_controls}")
        print(f"exact assertions: {COUNTS.exact_assertions}")
        print("mathematical authority: HUMAN PROOFS IN PACKET, NOT CHECK COUNTS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
