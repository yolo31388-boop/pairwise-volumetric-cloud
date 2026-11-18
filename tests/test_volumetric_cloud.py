import pytest
from render import volumetric_cloud as mod

CASES = [
    ("step_double", "m.world_step(2.0, 2.0) == approx(1.0)"),
    ("step_zero_scale", "m.world_step(2.0, 0.0) > 0.0"),
    ("depth_positive", "m.cloud_depth(2.0, 5.0) == approx(3.0)"),
    ("depth_reversed", "m.cloud_depth(5.0, 2.0) == approx(0.0)"),
    ("light_product", "m.light_sample(0.5, 4.0) == approx(2.0)"),
    ("shadow_same", "m.shadow_stable(1.0, 1.0) is True"),
    ("shadow_changed", "m.shadow_stable(1.0, 1.5) is False"),
    ("early_true", "m.early_out(0.01, 0.1) is True"),
    ("early_false", "m.early_out(0.5, 0.1) is False"),
    ("weight_sum", "m.depth_aware_weight(1.0, 2.0) + m.depth_aware_weight(2.0, 1.0) == approx(1.0)"),
    ("weight_near", "m.depth_aware_weight(1.0, 2.0) > m.depth_aware_weight(2.0, 1.0)"),
    ("wind_move", "m.wind_shift((1.0, 0.0), (2.0, 0.0), 0.5) == (2.0, 0.0)"),
    ("scatter_sum", "sum(m.normalize_scatter([2.0, 3.0])) == approx(1.0)"),
    ("scatter_equal", "m.normalize_scatter([2.0, 2.0])[0] == approx(0.5)"),
    ("depth_equal", "m.cloud_depth(3.0, 3.0) == approx(0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
