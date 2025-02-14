import pytest
import numpy as np
from polysolve import polysolve

def test_quadratic():
    """
    Tests that quadratic finds the root for a known problem.
    """
    params = [3.,0.,-1.]
    roots = quadratic(*params)
    assert all(np.isclose(np.polyval(params, root), 0.) for root in roots)

def test_quadratic_fails():
    """
    Check bad quadratic raises error.
    """
    with pytest.raises(ValueError)