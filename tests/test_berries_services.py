import pytest
from services.berries_service import (
    compute_stats,
    get_all_berry_stats
)
from config import POKEAPI_BASE_URL

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


def test_get_all_berry_stats(requests_mock):
    berry_list_url = f"{POKEAPI_BASE_URL}/berry/"
    berry_1 = f"{POKEAPI_BASE_URL}/berry/1/"
    berry_2 = f"{POKEAPI_BASE_URL}/berry/2/"

    requests_mock.get(
        berry_list_url,
        json={
            "results": [
                {"name": "cheri", "url": berry_1},
                {"name": "chesto", "url": berry_2}
            ],
            "next": None
        }
    )
    requests_mock.get(berry_1, json={"name": "cheri", "growth_time": 3})
    requests_mock.get(berry_2, json={"name": "chesto", "growth_time": 6})

    result = get_all_berry_stats()
    assert result["berries_names"] == ["cheri", "chesto"]
    assert result["min_growth_time"] == 3
    assert result["max_growth_time"] == 6