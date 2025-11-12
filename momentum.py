#!/usr/bin/env python3
"""
Momentum - A Life-Changing Personal Development CLI Tool
Transform your life one day at a time.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict
import sys

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, BarColumn, TextColumn
    from rich.prompt import Prompt, Confirm, IntPrompt
    from rich.layout import Layout
    from rich.align import Align
    from rich import box
    from rich.text import Text
except ImportError:
    print("Installing required dependencies...")
    os.system(f"{sys.executable} -m pip install rich --quiet")
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, BarColumn, TextColumn
    from rich.prompt import Prompt, Confirm, IntPrompt
    from rich.layout import Layout
    from rich.align import Align
    from rich import box
    from rich.text import Text

console = Console()

# Data file path
DATA_DIR = Path.home() / ".momentum"
DATA_FILE = DATA_DIR / "data.json"

# Motivational quotes
QUOTES = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Success is the sum of small efforts repeated day in and day out. - Robert Collier",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future depends on what you do today. - Mahatma Gandhi",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Small daily improvements are the key to staggering long-term results.",
    "Your life does not get better by chance, it gets better by change.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "You don't have to be great to start, but you have to start to be great.",
    "Progress, not perfection.",
    "Each day is a new opportunity to become a better version of yourself.",
]


class MomentumData:
    """Manages all data persistence"""

    def __init__(self):
        self.data = self.load_data()

    def load_data(self) -> dict:
        """Load data from JSON file"""
        if not DATA_DIR.exists():
            DATA_DIR.mkdir(parents=True)

        if not DATA_FILE.exists():
            return self.get_default_data()

        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return self.get_default_data()

    def get_default_data(self) -> dict:
        """Return default data structure"""
        return {
            "goals": [],
            "habits": [],
            "journal_entries": [],
            "mood_logs": [],
            "stats": {
                "total_days_active": 0,
                "total_goals_completed": 0,
                "total_habits_completed": 0,
                "level": 1,
                "xp": 0,
                "badges": []
            },
            "created_at": datetime.now().isoformat()
        }

    def save_data(self):
        """Save data to JSON file"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)


class Momentum:
    """Main application class"""

    def __init__(self):
        self.db = MomentumData()
        self.today = datetime.now().date().isoformat()

    def run(self):
        """Main application loop"""
        self.show_welcome()

        while True:
            choice = self.show_main_menu()

            if choice == "1":
                self.daily_checkin()
            elif choice == "2":
                self.manage_goals()
            elif choice == "3":
                self.manage_habits()
            elif choice == "4":
                self.journal()
            elif choice == "5":
                self.track_mood()
            elif choice == "6":
                self.view_progress()
            elif choice == "7":
                self.view_insights()
            elif choice == "8":
                self.show_motivation()
            elif choice == "9":
                console.print("\n[bold green]Keep building momentum! 🚀[/bold green]\n")
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")

    def show_welcome(self):
        """Display welcome screen"""
        console.clear()

        # Get user's level and XP
        level = self.db.data["stats"]["level"]
        xp = self.db.data["stats"]["xp"]
        next_level_xp = level * 100

        welcome_text = Text()
        welcome_text.append("✨ MOMENTUM ✨\n", style="bold cyan")
        welcome_text.append("Transform Your Life, One Day at a Time\n", style="italic")
        welcome_text.append(f"\nLevel {level} | XP: {xp}/{next_level_xp}", style="yellow")

        panel = Panel(
            Align.center(welcome_text),
            border_style="cyan",
            box=box.DOUBLE
        )
        console.print(panel)
        console.print()

        # Show daily quote
        import random
        quote = random.choice(QUOTES)
        console.print(Panel(f"[italic]{quote}[/italic]", border_style="blue", title="Daily Inspiration"))
        console.print()

    def show_main_menu(self) -> str:
        """Display main menu and get user choice"""
        table = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
        table.add_column("Option", style="cyan")
        table.add_column("Description")

        table.add_row("1", "📋 Daily Check-in (Morning/Evening)")
        table.add_row("2", "🎯 Manage Goals")
        table.add_row("3", "⚡ Manage Habits")
        table.add_row("4", "📝 Journal Entry")
        table.add_row("5", "😊 Track Mood & Energy")
        table.add_row("6", "📊 View Progress")
        table.add_row("7", "💡 Insights & Analytics")
        table.add_row("8", "🌟 Get Motivated")
        table.add_row("9", "Exit")

        console.print(table)
        return Prompt.ask("\n[bold]Choose an option[/bold]", default="1")

    def daily_checkin(self):
        """Morning intentions and evening reflections"""
        console.clear()
        console.print(Panel("[bold]Daily Check-in[/bold]", border_style="green"))

        checkin_type = Prompt.ask(
            "\nWhat would you like to do?",
            choices=["morning", "evening", "back"],
            default="morning"
        )

        if checkin_type == "back":
            return

        if checkin_type == "morning":
            self.morning_checkin()
        else:
            self.evening_checkin()

    def morning_checkin(self):
        """Morning intentions"""
        console.print("\n[bold cyan]🌅 Morning Check-in[/bold cyan]\n")

        # Set intentions
        console.print("[yellow]What are your top 3 intentions for today?[/yellow]")
        intentions = []
        for i in range(3):
            intention = Prompt.ask(f"  {i+1}.")
            if intention:
                intentions.append(intention)

        # Gratitude
        gratitude = Prompt.ask("\n[yellow]What are you grateful for today?[/yellow]")

        # Energy level
        energy = IntPrompt.ask("\n[yellow]How's your energy level? (1-10)[/yellow]", default=7)

        # Save
        entry = {
            "date": self.today,
            "type": "morning",
            "intentions": intentions,
            "gratitude": gratitude,
            "energy": energy,
            "timestamp": datetime.now().isoformat()
        }

        self.db.data["journal_entries"].append(entry)
        self.add_xp(10, "Morning check-in completed! ☀️")
        self.db.save_data()

        console.print("\n[bold green]✓ Morning check-in complete! Have an amazing day! 🚀[/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def evening_checkin(self):
        """Evening reflection"""
        console.print("\n[bold magenta]🌙 Evening Reflection[/bold magenta]\n")

        # Review day
        wins = Prompt.ask("[yellow]What were your wins today?[/yellow]")
        learned = Prompt.ask("[yellow]What did you learn?[/yellow]")
        improve = Prompt.ask("[yellow]What could you improve tomorrow?[/yellow]")

        # Mood
        mood = Prompt.ask(
            "\n[yellow]How would you rate your day?[/yellow]",
            choices=["great", "good", "okay", "difficult"],
            default="good"
        )

        # Save
        entry = {
            "date": self.today,
            "type": "evening",
            "wins": wins,
            "learned": learned,
            "improve": improve,
            "mood": mood,
            "timestamp": datetime.now().isoformat()
        }

        self.db.data["journal_entries"].append(entry)
        self.add_xp(10, "Evening reflection completed! 🌙")
        self.db.save_data()

        console.print("\n[bold green]✓ Evening reflection complete! Rest well! 😴[/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def manage_goals(self):
        """Goal management"""
        while True:
            console.clear()
            console.print(Panel("[bold]🎯 Goal Management[/bold]", border_style="cyan"))

            # Show existing goals
            self.display_goals()

            console.print("\n[cyan]1.[/cyan] Add new goal")
            console.print("[cyan]2.[/cyan] Update goal progress")
            console.print("[cyan]3.[/cyan] Complete goal")
            console.print("[cyan]4.[/cyan] Delete goal")
            console.print("[cyan]5.[/cyan] Back to main menu")

            choice = Prompt.ask("\nChoose an option", default="5")

            if choice == "1":
                self.add_goal()
            elif choice == "2":
                self.update_goal_progress()
            elif choice == "3":
                self.complete_goal()
            elif choice == "4":
                self.delete_goal()
            elif choice == "5":
                break

    def display_goals(self):
        """Display all goals"""
        goals = self.db.data["goals"]
        active_goals = [g for g in goals if not g.get("completed", False)]

        if not active_goals:
            console.print("\n[yellow]No active goals yet. Create your first goal![/yellow]")
            return

        table = Table(title="\nYour Goals", box=box.ROUNDED)
        table.add_column("#", style="cyan")
        table.add_column("Goal", style="white")
        table.add_column("Category", style="yellow")
        table.add_column("Progress", style="green")
        table.add_column("Deadline", style="magenta")

        for idx, goal in enumerate(active_goals, 1):
            progress = goal.get("progress", 0)
            target = goal.get("target", 100)
            progress_bar = self.create_progress_bar(progress, target)
            deadline = goal.get("deadline", "No deadline")

            table.add_row(
                str(idx),
                goal["title"],
                goal.get("category", "General"),
                progress_bar,
                deadline
            )

        console.print(table)

    def create_progress_bar(self, current: int, target: int, width: int = 20) -> str:
        """Create a text progress bar"""
        percentage = min(100, int((current / target) * 100))
        filled = int((percentage / 100) * width)
        bar = "█" * filled + "░" * (width - filled)
        return f"{bar} {percentage}%"

    def add_goal(self):
        """Add a new goal"""
        console.print("\n[bold]Create a New Goal[/bold]\n")

        title = Prompt.ask("[yellow]Goal title[/yellow]")
        category = Prompt.ask(
            "[yellow]Category[/yellow]",
            choices=["health", "career", "finance", "learning", "relationships", "personal"],
            default="personal"
        )
        description = Prompt.ask("[yellow]Description (optional)[/yellow]", default="")
        target = IntPrompt.ask("[yellow]Target value (for tracking progress)[/yellow]", default=100)
        deadline = Prompt.ask("[yellow]Deadline (YYYY-MM-DD, optional)[/yellow]", default="")

        goal = {
            "id": len(self.db.data["goals"]) + 1,
            "title": title,
            "category": category,
            "description": description,
            "target": target,
            "progress": 0,
            "deadline": deadline,
            "created_at": datetime.now().isoformat(),
            "completed": False
        }

        self.db.data["goals"].append(goal)
        self.add_xp(20, "New goal created! 🎯")
        self.db.save_data()

        console.print(f"\n[bold green]✓ Goal '{title}' created successfully![/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def update_goal_progress(self):
        """Update progress on a goal"""
        goals = [g for g in self.db.data["goals"] if not g.get("completed", False)]
        if not goals:
            console.print("\n[yellow]No active goals to update.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        goal_num = IntPrompt.ask("\n[yellow]Enter goal number to update[/yellow]")
        if goal_num < 1 or goal_num > len(goals):
            console.print("[red]Invalid goal number.[/red]")
            Prompt.ask("\nPress Enter to continue")
            return

        goal = goals[goal_num - 1]
        current = goal["progress"]
        target = goal["target"]

        console.print(f"\nCurrent progress: {current}/{target}")
        new_progress = IntPrompt.ask("[yellow]Enter new progress value[/yellow]", default=current)

        goal["progress"] = new_progress

        xp_gained = 10
        if new_progress >= target:
            console.print("\n[bold green]🎉 Goal target reached! Consider completing this goal![/bold green]")
            xp_gained = 30

        self.add_xp(xp_gained, f"Progress updated on '{goal['title']}'!")
        self.db.save_data()

        Prompt.ask("\nPress Enter to continue")

    def complete_goal(self):
        """Mark a goal as completed"""
        goals = [g for g in self.db.data["goals"] if not g.get("completed", False)]
        if not goals:
            console.print("\n[yellow]No active goals to complete.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        goal_num = IntPrompt.ask("\n[yellow]Enter goal number to complete[/yellow]")
        if goal_num < 1 or goal_num > len(goals):
            console.print("[red]Invalid goal number.[/red]")
            Prompt.ask("\nPress Enter to continue")
            return

        goal = goals[goal_num - 1]
        goal["completed"] = True
        goal["completed_at"] = datetime.now().isoformat()

        self.db.data["stats"]["total_goals_completed"] += 1
        self.add_xp(50, f"🎉 Goal '{goal['title']}' COMPLETED! Amazing work!")
        self.db.save_data()

        # Celebration
        console.print(Panel(
            f"[bold green]🎊 CONGRATULATIONS! 🎊[/bold green]\n\n"
            f"You completed: [bold]{goal['title']}[/bold]\n\n"
            f"[italic]You're making incredible progress![/italic]",
            border_style="green",
            box=box.DOUBLE
        ))

        Prompt.ask("\nPress Enter to continue")

    def delete_goal(self):
        """Delete a goal"""
        goals = self.db.data["goals"]
        if not goals:
            console.print("\n[yellow]No goals to delete.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        goal_num = IntPrompt.ask("\n[yellow]Enter goal number to delete[/yellow]")
        active_goals = [g for g in goals if not g.get("completed", False)]

        if goal_num < 1 or goal_num > len(active_goals):
            console.print("[red]Invalid goal number.[/red]")
            Prompt.ask("\nPress Enter to continue")
            return

        goal = active_goals[goal_num - 1]
        if Confirm.ask(f"Are you sure you want to delete '{goal['title']}'?"):
            self.db.data["goals"].remove(goal)
            self.db.save_data()
            console.print("[green]Goal deleted.[/green]")

        Prompt.ask("\nPress Enter to continue")

    def manage_habits(self):
        """Habit management"""
        while True:
            console.clear()
            console.print(Panel("[bold]⚡ Habit Tracker[/bold]", border_style="yellow"))

            # Show existing habits
            self.display_habits()

            console.print("\n[cyan]1.[/cyan] Add new habit")
            console.print("[cyan]2.[/cyan] Log habit completion (today)")
            console.print("[cyan]3.[/cyan] View habit history")
            console.print("[cyan]4.[/cyan] Delete habit")
            console.print("[cyan]5.[/cyan] Back to main menu")

            choice = Prompt.ask("\nChoose an option", default="5")

            if choice == "1":
                self.add_habit()
            elif choice == "2":
                self.log_habit()
            elif choice == "3":
                self.view_habit_history()
            elif choice == "4":
                self.delete_habit()
            elif choice == "5":
                break

    def display_habits(self):
        """Display all habits"""
        habits = self.db.data["habits"]

        if not habits:
            console.print("\n[yellow]No habits yet. Create your first habit![/yellow]")
            return

        table = Table(title="\nYour Habits", box=box.ROUNDED)
        table.add_column("#", style="cyan")
        table.add_column("Habit", style="white")
        table.add_column("Frequency", style="yellow")
        table.add_column("Current Streak", style="green")
        table.add_column("Best Streak", style="magenta")
        table.add_column("Done Today?", style="blue")

        for idx, habit in enumerate(habits, 1):
            current_streak = self.calculate_streak(habit)
            best_streak = habit.get("best_streak", 0)
            done_today = self.today in habit.get("completed_dates", [])

            table.add_row(
                str(idx),
                habit["name"],
                habit["frequency"],
                f"🔥 {current_streak}",
                f"⭐ {best_streak}",
                "✅" if done_today else "⬜"
            )

        console.print(table)

    def calculate_streak(self, habit: dict) -> int:
        """Calculate current streak for a habit"""
        completed_dates = habit.get("completed_dates", [])
        if not completed_dates:
            return 0

        # Sort dates in reverse
        sorted_dates = sorted(completed_dates, reverse=True)

        streak = 0
        check_date = datetime.now().date()

        for date_str in sorted_dates:
            date = datetime.fromisoformat(date_str).date()
            if date == check_date:
                streak += 1
                check_date -= timedelta(days=1)
            elif date < check_date:
                break

        return streak

    def add_habit(self):
        """Add a new habit"""
        console.print("\n[bold]Create a New Habit[/bold]\n")

        name = Prompt.ask("[yellow]Habit name[/yellow]")
        frequency = Prompt.ask(
            "[yellow]Frequency[/yellow]",
            choices=["daily", "weekly", "custom"],
            default="daily"
        )

        habit = {
            "id": len(self.db.data["habits"]) + 1,
            "name": name,
            "frequency": frequency,
            "completed_dates": [],
            "best_streak": 0,
            "created_at": datetime.now().isoformat()
        }

        self.db.data["habits"].append(habit)
        self.add_xp(15, f"New habit '{name}' created! ⚡")
        self.db.save_data()

        console.print(f"\n[bold green]✓ Habit '{name}' created successfully![/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def log_habit(self):
        """Log habit completion for today"""
        habits = self.db.data["habits"]
        if not habits:
            console.print("\n[yellow]No habits to log.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        habit_num = IntPrompt.ask("\n[yellow]Enter habit number to log[/yellow]")
        if habit_num < 1 or habit_num > len(habits):
            console.print("[red]Invalid habit number.[/red]")
            Prompt.ask("\nPress Enter to continue")
            return

        habit = habits[habit_num - 1]

        if self.today in habit.get("completed_dates", []):
            console.print(f"\n[yellow]You already logged '{habit['name']}' today![/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        if "completed_dates" not in habit:
            habit["completed_dates"] = []

        habit["completed_dates"].append(self.today)

        # Update streak
        current_streak = self.calculate_streak(habit)
        if current_streak > habit.get("best_streak", 0):
            habit["best_streak"] = current_streak
            console.print(f"\n[bold magenta]🏆 NEW BEST STREAK: {current_streak} days! 🏆[/bold magenta]")

        self.db.data["stats"]["total_habits_completed"] += 1
        self.add_xp(15, f"✅ Habit '{habit['name']}' completed!")
        self.db.save_data()

        console.print(f"\n[bold green]✓ Great job! Current streak: {current_streak} days! 🔥[/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def view_habit_history(self):
        """View habit completion history"""
        habits = self.db.data["habits"]
        if not habits:
            console.print("\n[yellow]No habits to view.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        habit_num = IntPrompt.ask("\n[yellow]Enter habit number to view history[/yellow]")
        if habit_num < 1 or habit_num > len(habits):
            console.print("[red]Invalid habit number.[/red]")
            Prompt.ask("\nPress Enter to continue")
            return

        habit = habits[habit_num - 1]
        completed_dates = habit.get("completed_dates", [])

        console.print(f"\n[bold]History for: {habit['name']}[/bold]")
        console.print(f"Total completions: {len(completed_dates)}")
        console.print(f"Current streak: {self.calculate_streak(habit)} days")
        console.print(f"Best streak: {habit.get('best_streak', 0)} days")

        if completed_dates:
            console.print("\nRecent completions:")
            for date in sorted(completed_dates, reverse=True)[:10]:
                console.print(f"  ✓ {date}")

        Prompt.ask("\nPress Enter to continue")

    def delete_habit(self):
        """Delete a habit"""
        habits = self.db.data["habits"]
        if not habits:
            console.print("\n[yellow]No habits to delete.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        habit_num = IntPrompt.ask("\n[yellow]Enter habit number to delete[/yellow]")
        if habit_num < 1 or habit_num > len(habits):
            console.print("[red]Invalid habit number.[/red]")
            Prompt.ask("\nPress Enter to continue")
            return

        habit = habits[habit_num - 1]
        if Confirm.ask(f"Are you sure you want to delete '{habit['name']}'?"):
            self.db.data["habits"].remove(habit)
            self.db.save_data()
            console.print("[green]Habit deleted.[/green]")

        Prompt.ask("\nPress Enter to continue")

    def journal(self):
        """Free-form journaling"""
        console.clear()
        console.print(Panel("[bold]📝 Journal[/bold]", border_style="blue"))

        console.print("\n[cyan]1.[/cyan] Write new entry")
        console.print("[cyan]2.[/cyan] View recent entries")
        console.print("[cyan]3.[/cyan] Back")

        choice = Prompt.ask("\nChoose an option", default="3")

        if choice == "1":
            self.write_journal_entry()
        elif choice == "2":
            self.view_journal_entries()

    def write_journal_entry(self):
        """Write a journal entry"""
        console.print("\n[bold]Write Your Journal Entry[/bold]")
        console.print("[dim]Type your thoughts. Press Enter twice when done.[/dim]\n")

        lines = []
        empty_count = 0

        while empty_count < 2:
            line = Prompt.ask("", default="")
            if not line:
                empty_count += 1
            else:
                empty_count = 0
                lines.append(line)

        content = "\n".join(lines)

        if not content.strip():
            console.print("[yellow]No content entered.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        entry = {
            "date": self.today,
            "type": "journal",
            "content": content,
            "timestamp": datetime.now().isoformat()
        }

        self.db.data["journal_entries"].append(entry)
        self.add_xp(10, "Journal entry saved! 📝")
        self.db.save_data()

        console.print("\n[bold green]✓ Journal entry saved![/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def view_journal_entries(self):
        """View recent journal entries"""
        entries = [e for e in self.db.data["journal_entries"] if e.get("type") == "journal"]

        if not entries:
            console.print("\n[yellow]No journal entries yet.[/yellow]")
            Prompt.ask("\nPress Enter to continue")
            return

        console.print("\n[bold]Recent Journal Entries[/bold]\n")

        for entry in sorted(entries, key=lambda x: x["timestamp"], reverse=True)[:5]:
            date = entry["date"]
            content = entry["content"][:200] + "..." if len(entry["content"]) > 200 else entry["content"]

            console.print(Panel(
                f"[dim]{date}[/dim]\n\n{content}",
                border_style="blue"
            ))

        Prompt.ask("\nPress Enter to continue")

    def track_mood(self):
        """Track mood and energy"""
        console.clear()
        console.print(Panel("[bold]😊 Mood & Energy Tracker[/bold]", border_style="magenta"))

        console.print("\n[bold]How are you feeling right now?[/bold]\n")

        mood = Prompt.ask(
            "[yellow]Overall mood[/yellow]",
            choices=["amazing", "good", "okay", "down", "struggling"],
            default="good"
        )

        energy = IntPrompt.ask("[yellow]Energy level (1-10)[/yellow]", default=5)
        stress = IntPrompt.ask("[yellow]Stress level (1-10)[/yellow]", default=5)
        notes = Prompt.ask("[yellow]Any notes? (optional)[/yellow]", default="")

        log = {
            "date": self.today,
            "mood": mood,
            "energy": energy,
            "stress": stress,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        }

        self.db.data["mood_logs"].append(log)
        self.add_xp(5, "Mood logged! 😊")
        self.db.save_data()

        console.print("\n[bold green]✓ Mood logged! Taking care of your mental health is important! 💚[/bold green]")
        Prompt.ask("\nPress Enter to continue")

    def view_progress(self):
        """View overall progress and statistics"""
        console.clear()
        console.print(Panel("[bold]📊 Your Progress[/bold]", border_style="cyan"))

        stats = self.db.data["stats"]

        # Create stats table
        table = Table(title="\nYour Statistics", box=box.ROUNDED)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="yellow")

        table.add_row("Level", str(stats["level"]))
        table.add_row("XP", f"{stats['xp']}/{stats['level'] * 100}")
        table.add_row("Goals Completed", str(stats["total_goals_completed"]))
        table.add_row("Habits Completed", str(stats["total_habits_completed"]))
        table.add_row("Active Goals", str(len([g for g in self.db.data["goals"] if not g.get("completed", False)])))
        table.add_row("Active Habits", str(len(self.db.data["habits"])))
        table.add_row("Journal Entries", str(len(self.db.data["journal_entries"])))
        table.add_row("Mood Logs", str(len(self.db.data["mood_logs"])))

        console.print(table)

        # Show badges
        if stats.get("badges"):
            console.print("\n[bold]🏆 Badges Earned:[/bold]")
            for badge in stats["badges"]:
                console.print(f"  {badge}")

        Prompt.ask("\nPress Enter to continue")

    def view_insights(self):
        """View insights and analytics"""
        console.clear()
        console.print(Panel("[bold]💡 Insights & Analytics[/bold]", border_style="yellow"))

        # Mood trends
        mood_logs = self.db.data["mood_logs"]
        if mood_logs:
            recent_moods = mood_logs[-7:]  # Last 7 entries
            avg_energy = sum(m["energy"] for m in recent_moods) / len(recent_moods)
            avg_stress = sum(m["stress"] for m in recent_moods) / len(recent_moods)

            console.print("\n[bold]Recent Trends (Last 7 logs):[/bold]")
            console.print(f"  Average Energy: {avg_energy:.1f}/10")
            console.print(f"  Average Stress: {avg_stress:.1f}/10")

        # Habit consistency
        habits = self.db.data["habits"]
        if habits:
            console.print("\n[bold]Habit Streaks:[/bold]")
            for habit in habits:
                streak = self.calculate_streak(habit)
                if streak > 0:
                    console.print(f"  🔥 {habit['name']}: {streak} days")

        # Goals progress
        goals = [g for g in self.db.data["goals"] if not g.get("completed", False)]
        if goals:
            console.print("\n[bold]Goals Nearing Completion:[/bold]")
            for goal in goals:
                percentage = (goal["progress"] / goal["target"]) * 100
                if percentage >= 75:
                    console.print(f"  🎯 {goal['title']}: {percentage:.0f}% complete")

        # Motivational insight
        stats = self.db.data["stats"]
        total_actions = (stats["total_goals_completed"] +
                        stats["total_habits_completed"] +
                        len(self.db.data["journal_entries"]))

        console.print(f"\n[bold green]You've taken {total_actions} positive actions with Momentum! 🚀[/bold green]")

        Prompt.ask("\nPress Enter to continue")

    def show_motivation(self):
        """Show motivational message"""
        console.clear()

        import random
        quote = random.choice(QUOTES)

        stats = self.db.data["stats"]
        level = stats["level"]

        messages = [
            f"You're at Level {level}! Keep crushing it! 💪",
            "Every small step counts. You're doing amazing! 🌟",
            "Progress over perfection. Keep going! 🚀",
            "You're building the life you deserve, one day at a time! ✨",
            "Your consistency is your superpower! ⚡",
        ]

        message = random.choice(messages)

        panel = Panel(
            f"[bold cyan]{message}[/bold cyan]\n\n"
            f"[italic]{quote}[/italic]",
            title="🌟 Motivation 🌟",
            border_style="yellow",
            box=box.DOUBLE
        )

        console.print(panel)
        Prompt.ask("\nPress Enter to continue")

    def add_xp(self, amount: int, message: str = ""):
        """Add XP and handle leveling"""
        stats = self.db.data["stats"]
        stats["xp"] += amount

        # Check for level up
        next_level_xp = stats["level"] * 100

        if stats["xp"] >= next_level_xp:
            stats["level"] += 1
            stats["xp"] = stats["xp"] - next_level_xp

            console.print(Panel(
                f"[bold yellow]🎉 LEVEL UP! 🎉[/bold yellow]\n\n"
                f"You're now Level {stats['level']}!\n\n"
                f"[italic]You're becoming unstoppable![/italic]",
                border_style="yellow",
                box=box.DOUBLE
            ))

        if message:
            console.print(f"[green]+{amount} XP | {message}[/green]")


def main():
    """Main entry point"""
    try:
        app = Momentum()
        app.run()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Session interrupted. Your progress is saved! 💾[/yellow]")
    except Exception as e:
        console.print(f"\n[red]An error occurred: {e}[/red]")
        console.print("[yellow]Don't worry, your data is safe![/yellow]")


if __name__ == "__main__":
    main()
