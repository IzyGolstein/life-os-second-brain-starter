# ML Review Checklist

Use this checklist only when the main skill needs detail.

## Formalization

- Unit of analysis.
- Treatment/action space.
- Outcome and horizon.
- Target estimand.
- Decision objective.
- Loss function.
- Evaluation metric.
- Baseline.

## Failure Modes

- Label does not identify the claimed latent variable.
- Prediction metric does not match policy value.
- Treatment propensity is missing or wrong.
- Feature leakage or post-treatment features.
- Calibration differs by treatment arm.
- Monotonicity assumed but not tested.
- Offline evaluation has low overlap or high variance.
- Model improvement disappears under iso-budget comparison.

## Minimum Experiment

- One stable validation slice.
- Clean baseline.
- New model.
- Cheap ablation.
- Policy-value comparison.
- Bootstrap confidence interval.
- Stop/go criterion before implementation expands.
