import pytest
from services.berries_service import (
    compute_stats
)
def test_compute_stats_empty_list():
    """Test compute_stats with empty list returns default values."""
    result = compute_stats([])
    assert result == {
        'min_growth_time': 0,
        'max_growth_time': 0,
        'median_growth_time': 0.0,
        'mean_growth_time': 0.0,
        'variance_growth_time': 0.0,
        'frequency_growth_time': {}
    }


def test_compute_stats_single_element():
    """Test compute_stats with single element."""
    result = compute_stats([5])
    assert result['min_growth_time'] == 5
    assert result['max_growth_time'] == 5
    assert result['mean_growth_time'] == 5.0
    assert result['median_growth_time'] == 5.0
    assert result['variance_growth_time'] == 0.0
    assert result['frequency_growth_time'] == {5: 1}


def test_compute_stats_multiple_elements():
    """Test compute_stats with multiple elements."""
    result = compute_stats([3, 5, 3, 7, 5])
    assert result['min_growth_time'] == 3
    assert result['max_growth_time'] == 7
    assert result['mean_growth_time'] == 4.6
    assert result['median_growth_time'] == 5.0
    assert result['variance_growth_time'] > 0
    assert result['frequency_growth_time'] == {3: 2, 5: 2, 7: 1}


def test_compute_stats_variance_with_two_elements():
    """Test compute_stats variance calculation with two elements."""
    result = compute_stats([3, 7])
    assert result['variance_growth_time'] > 0
    assert result['mean_growth_time'] == 5.0


