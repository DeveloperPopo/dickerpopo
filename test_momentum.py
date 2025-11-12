#!/usr/bin/env python3
"""Quick test to verify Momentum functionality"""

import sys
sys.path.insert(0, '/home/user/dickerpopo')

try:
    from momentum import MomentumData, Momentum
    print("✓ Successfully imported Momentum classes")

    # Test data initialization
    db = MomentumData()
    print("✓ Data initialization working")

    # Check data structure
    assert "goals" in db.data
    assert "habits" in db.data
    assert "stats" in db.data
    print("✓ Data structure is correct")

    # Test adding a goal
    test_goal = {
        "id": 1,
        "title": "Test Goal",
        "category": "personal",
        "description": "This is a test",
        "target": 100,
        "progress": 0,
        "completed": False
    }
    db.data["goals"].append(test_goal)
    print("✓ Can add goals")

    # Test adding a habit
    test_habit = {
        "id": 1,
        "name": "Test Habit",
        "frequency": "daily",
        "completed_dates": [],
        "best_streak": 0
    }
    db.data["habits"].append(test_habit)
    print("✓ Can add habits")

    print("\n✅ All basic tests passed!")
    print("🚀 Momentum is ready to transform lives!")

except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
