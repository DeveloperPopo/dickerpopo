#!/usr/bin/env python3
"""
Heartbeat - The Ultimate Relationship & Connection Management Tool

Research shows that the quality of our relationships is THE #1 predictor of
happiness, health, and longevity. Heartbeat helps you nurture and maintain
the connections that matter most in your life.

Because the best thing a human ever needs is love, connection, and belonging.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import sys

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, Confirm
    from rich.progress import Progress, BarColumn, TextColumn
    from rich import box
    from rich.layout import Layout
    from rich.text import Text
except ImportError:
    print("📦 Installing required dependency: rich")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, Confirm
    from rich.progress import Progress, BarColumn, TextColumn
    from rich import box
    from rich.layout import Layout
    from rich.text import Text

console = Console()

# Data directory
DATA_DIR = Path.home() / ".heartbeat"
DATA_FILE = DATA_DIR / "data.json"

# Default data structure
DEFAULT_DATA = {
    "profile": {
        "name": "",
        "level": 1,
        "xp": 0,
        "total_connections": 0,
        "total_kindness_acts": 0,
        "created_at": datetime.now().isoformat()
    },
    "relationships": {},  # person_id -> relationship data
    "interactions": [],    # list of interaction events
    "kindness_acts": [],   # list of kind acts
    "connection_goals": [],  # goals for relationship maintenance
    "milestones": []       # achievements and special moments
}

# Relationship types
RELATIONSHIP_TYPES = [
    "Family", "Close Friend", "Friend", "Romantic Partner",
    "Colleague", "Mentor", "Acquaintance", "Community"
]

# Interaction types
INTERACTION_TYPES = [
    "In-Person", "Phone Call", "Video Call", "Text/Message",
    "Social Media", "Email", "Quality Time", "Group Hangout"
]

# Connection frequencies (suggested)
CONNECTION_FREQUENCIES = {
    "Daily": 1,
    "Every Few Days": 3,
    "Weekly": 7,
    "Bi-Weekly": 14,
    "Monthly": 30,
    "Quarterly": 90,
    "Yearly": 365
}

# XP rewards
XP_REWARDS = {
    "add_person": 25,
    "log_interaction": 15,
    "quality_time": 30,
    "kindness_act": 20,
    "reach_out_reminder": 10,
    "connection_goal": 50,
    "birthday_remembered": 40,
    "meaningful_conversation": 35
}

# Inspirational quotes about relationships
RELATIONSHIP_QUOTES = [
    "The best thing to hold onto in life is each other. - Audrey Hepburn",
    "The greatest gift of life is friendship. - Hubert H. Humphrey",
    "Connection is why we're here. It gives purpose and meaning to our lives. - Brené Brown",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - MLK",
    "The quality of your life is the quality of your relationships. - Tony Robbins",
    "Love is that condition in which the happiness of another person is essential to your own. - Robert Heinlein",
    "A single rose can be my garden... a single friend, my world. - Leo Buscaglia",
    "The most important thing in life is to learn how to give out love, and to let it come in. - Morrie Schwartz",
    "We are all connected. What we do to others, we do to ourselves. - Unknown",
    "The meeting of two personalities is like the contact of two chemical substances. - Carl Jung"
]


class HeartbeatApp:
    """Main application class for Heartbeat"""

    def __init__(self):
        self.data = self.load_data()

    def load_data(self) -> Dict:
        """Load data from JSON file or create default"""
        if not DATA_DIR.exists():
            DATA_DIR.mkdir(parents=True)

        if not DATA_FILE.exists():
            # First time setup
            console.print(Panel.fit(
                "[bold cyan]Welcome to Heartbeat! ❤️[/bold cyan]\n\n"
                "The tool that helps you nurture the most important thing in life:\n"
                "[bold]Your relationships and connections.[/bold]\n\n"
                "Let's get you set up!",
                border_style="cyan"
            ))

            name = Prompt.ask("What's your name?", default="Friend")

            data = DEFAULT_DATA.copy()
            data["profile"]["name"] = name

            self.save_data(data)

            console.print(Panel.fit(
                f"[bold green]Welcome, {name}! 🌟[/bold green]\n\n"
                "Your data will be stored securely at:\n"
                f"[dim]{DATA_FILE}[/dim]\n\n"
                "Let's start building meaningful connections!",
                border_style="green"
            ))

            return data

        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def save_data(self, data: Optional[Dict] = None):
        """Save data to JSON file"""
        if data is None:
            data = self.data

        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def add_xp(self, amount: int, reason: str = ""):
        """Add XP and check for level up"""
        self.data["profile"]["xp"] += amount
        current_level = self.data["profile"]["level"]
        xp_needed = current_level * 100

        if self.data["profile"]["xp"] >= xp_needed:
            self.data["profile"]["level"] += 1
            self.data["profile"]["xp"] -= xp_needed
            self.save_data()
            self.show_level_up()
        else:
            self.save_data()
            if reason:
                console.print(f"[green]+{amount} XP[/green] - {reason}")

    def show_level_up(self):
        """Display level up celebration"""
        level = self.data["profile"]["level"]
        console.print(Panel.fit(
            f"[bold yellow]🎉 LEVEL UP! 🎉[/bold yellow]\n\n"
            f"[bold cyan]You are now Level {level}![/bold cyan]\n\n"
            "Your commitment to nurturing relationships\n"
            "is making you a better human! Keep going! 💪❤️",
            border_style="yellow"
        ))

    def generate_person_id(self, name: str) -> str:
        """Generate unique ID for a person"""
        base_id = name.lower().replace(" ", "_")
        counter = 1
        person_id = base_id

        while person_id in self.data["relationships"]:
            person_id = f"{base_id}_{counter}"
            counter += 1

        return person_id

    def add_relationship(self):
        """Add a new relationship"""
        console.print(Panel.fit(
            "[bold cyan]Add New Relationship 👥[/bold cyan]\n\n"
            "Let's add someone important to your life!",
            border_style="cyan"
        ))

        name = Prompt.ask("Person's name")

        # Relationship type
        console.print("\n[bold]Relationship Type:[/bold]")
        for i, rel_type in enumerate(RELATIONSHIP_TYPES, 1):
            console.print(f"{i}. {rel_type}")

        type_choice = Prompt.ask(
            "Choose type",
            choices=[str(i) for i in range(1, len(RELATIONSHIP_TYPES) + 1)]
        )
        relationship_type = RELATIONSHIP_TYPES[int(type_choice) - 1]

        # Closeness (1-10 scale)
        closeness = int(Prompt.ask(
            "Closeness level (1-10)",
            choices=[str(i) for i in range(1, 11)]
        ))

        # Optional details
        birthday = Prompt.ask("Birthday (MM-DD) [optional]", default="")
        interests = Prompt.ask("Interests/hobbies [optional]", default="")
        notes = Prompt.ask("Important notes [optional]", default="")

        # Desired contact frequency
        console.print("\n[bold]How often would you like to connect?[/bold]")
        for i, (freq, days) in enumerate(CONNECTION_FREQUENCIES.items(), 1):
            console.print(f"{i}. {freq}")

        freq_choice = Prompt.ask(
            "Choose frequency",
            choices=[str(i) for i in range(1, len(CONNECTION_FREQUENCIES) + 1)]
        )
        desired_frequency = list(CONNECTION_FREQUENCIES.keys())[int(freq_choice) - 1]
        frequency_days = list(CONNECTION_FREQUENCIES.values())[int(freq_choice) - 1]

        # Create relationship entry
        person_id = self.generate_person_id(name)

        self.data["relationships"][person_id] = {
            "name": name,
            "relationship_type": relationship_type,
            "closeness": closeness,
            "birthday": birthday,
            "interests": interests,
            "notes": notes,
            "desired_frequency": desired_frequency,
            "frequency_days": frequency_days,
            "last_contact": datetime.now().isoformat(),
            "added_date": datetime.now().isoformat(),
            "total_interactions": 0,
            "quality_time_hours": 0
        }

        self.add_xp(XP_REWARDS["add_person"], f"Added {name} to your circle")

        console.print(Panel.fit(
            f"[bold green]✅ {name} added successfully![/bold green]\n\n"
            f"Type: {relationship_type}\n"
            f"Closeness: {closeness}/10 ❤️\n"
            f"Connection goal: {desired_frequency}",
            border_style="green"
        ))

    def log_interaction(self):
        """Log an interaction with someone"""
        if not self.data["relationships"]:
            console.print("[yellow]⚠️  No relationships added yet. Add someone first![/yellow]")
            return

        console.print(Panel.fit(
            "[bold cyan]Log Interaction 💬[/bold cyan]\n\n"
            "Record a meaningful connection!",
            border_style="cyan"
        ))

        # Select person
        people = list(self.data["relationships"].items())
        console.print("\n[bold]Who did you connect with?[/bold]")
        for i, (person_id, person) in enumerate(people, 1):
            console.print(f"{i}. {person['name']} ({person['relationship_type']})")

        person_choice = int(Prompt.ask(
            "Choose person",
            choices=[str(i) for i in range(1, len(people) + 1)]
        ))
        person_id, person = people[person_choice - 1]

        # Interaction type
        console.print("\n[bold]Type of interaction:[/bold]")
        for i, interaction_type in enumerate(INTERACTION_TYPES, 1):
            console.print(f"{i}. {interaction_type}")

        type_choice = int(Prompt.ask(
            "Choose type",
            choices=[str(i) for i in range(1, len(INTERACTION_TYPES) + 1)]
        ))
        interaction_type = INTERACTION_TYPES[type_choice - 1]

        # Duration (for quality time)
        duration = 0
        if "Quality Time" in interaction_type or "In-Person" in interaction_type:
            duration = float(Prompt.ask("Duration in hours", default="1"))

        # Quality rating
        quality = int(Prompt.ask(
            "Quality of connection (1-10)",
            choices=[str(i) for i in range(1, 11)]
        ))

        # Notes
        notes = Prompt.ask("Notes about the interaction [optional]", default="")

        # Was it meaningful?
        meaningful = Confirm.ask("Was this a particularly meaningful conversation?")

        # Create interaction record
        interaction = {
            "person_id": person_id,
            "person_name": person["name"],
            "type": interaction_type,
            "duration_hours": duration,
            "quality": quality,
            "notes": notes,
            "meaningful": meaningful,
            "date": datetime.now().isoformat()
        }

        self.data["interactions"].append(interaction)

        # Update relationship data
        self.data["relationships"][person_id]["last_contact"] = datetime.now().isoformat()
        self.data["relationships"][person_id]["total_interactions"] += 1
        if duration > 0:
            self.data["relationships"][person_id]["quality_time_hours"] += duration

        # Update profile stats
        self.data["profile"]["total_connections"] += 1

        # Award XP
        xp = XP_REWARDS["log_interaction"]
        if duration >= 2:
            xp = XP_REWARDS["quality_time"]
        if meaningful:
            xp += XP_REWARDS["meaningful_conversation"]

        self.add_xp(xp, f"Connected with {person['name']}")

        console.print(Panel.fit(
            f"[bold green]✅ Interaction logged![/bold green]\n\n"
            f"Person: {person['name']}\n"
            f"Type: {interaction_type}\n"
            f"Quality: {quality}/10 {'⭐' * quality}\n"
            f"{'🌟 Meaningful conversation!' if meaningful else ''}",
            border_style="green"
        ))

    def log_kindness(self):
        """Log an act of kindness"""
        console.print(Panel.fit(
            "[bold cyan]Log Act of Kindness 🌟[/bold cyan]\n\n"
            "What kind thing did you do for someone?",
            border_style="cyan"
        ))

        # Select person (optional - can be for stranger)
        person_name = "Someone"
        person_id = None

        if self.data["relationships"]:
            include_person = Confirm.ask("Was this for someone in your contacts?")

            if include_person:
                people = list(self.data["relationships"].items())
                console.print("\n[bold]Who was it for?[/bold]")
                for i, (pid, person) in enumerate(people, 1):
                    console.print(f"{i}. {person['name']}")

                person_choice = int(Prompt.ask(
                    "Choose person",
                    choices=[str(i) for i in range(1, len(people) + 1)]
                ))
                person_id, person = people[person_choice - 1]
                person_name = person["name"]

        # Description of kindness
        description = Prompt.ask("What kind act did you do?")

        # Impact
        impact = Prompt.ask(
            "How much do you think it meant to them? (1-10)",
            choices=[str(i) for i in range(1, 11)]
        )

        # How it made you feel
        your_feeling = Prompt.ask("How did it make YOU feel? [optional]", default="")

        # Create kindness record
        kindness = {
            "person_id": person_id,
            "person_name": person_name,
            "description": description,
            "impact": int(impact),
            "your_feeling": your_feeling,
            "date": datetime.now().isoformat()
        }

        self.data["kindness_acts"].append(kindness)
        self.data["profile"]["total_kindness_acts"] += 1

        self.add_xp(XP_REWARDS["kindness_act"], f"Kind act for {person_name}")

        console.print(Panel.fit(
            f"[bold green]✅ Kindness logged![/bold green]\n\n"
            f"For: {person_name}\n"
            f"Impact: {impact}/10 {'❤️' * int(impact)}\n\n"
            "The world needs more people like you! 🌟",
            border_style="green"
        ))

    def view_relationships(self):
        """Display all relationships"""
        if not self.data["relationships"]:
            console.print("[yellow]⚠️  No relationships added yet.[/yellow]")
            return

        table = Table(title="Your Circle 👥", box=box.ROUNDED)
        table.add_column("Name", style="cyan")
        table.add_column("Type", style="magenta")
        table.add_column("Closeness", style="yellow")
        table.add_column("Last Contact", style="green")
        table.add_column("Status", style="white")

        now = datetime.now()

        for person_id, person in self.data["relationships"].items():
            last_contact = datetime.fromisoformat(person["last_contact"])
            days_since = (now - last_contact).days

            # Determine status
            if days_since <= person["frequency_days"]:
                status = "✅ On track"
                status_style = "green"
            elif days_since <= person["frequency_days"] * 1.5:
                status = "⚠️  Check in soon"
                status_style = "yellow"
            else:
                status = "❗ Needs attention"
                status_style = "red"

            closeness_hearts = "❤️" * person["closeness"]

            if days_since == 0:
                last_contact_str = "Today"
            elif days_since == 1:
                last_contact_str = "Yesterday"
            else:
                last_contact_str = f"{days_since} days ago"

            table.add_row(
                person["name"],
                person["relationship_type"],
                closeness_hearts,
                last_contact_str,
                f"[{status_style}]{status}[/{status_style}]"
            )

        console.print(table)

    def connection_reminders(self):
        """Show who needs attention"""
        if not self.data["relationships"]:
            console.print("[yellow]⚠️  No relationships added yet.[/yellow]")
            return

        now = datetime.now()
        needs_attention = []

        for person_id, person in self.data["relationships"].items():
            last_contact = datetime.fromisoformat(person["last_contact"])
            days_since = (now - last_contact).days

            if days_since > person["frequency_days"]:
                needs_attention.append({
                    "person": person,
                    "days": days_since,
                    "overdue": days_since - person["frequency_days"]
                })

        if not needs_attention:
            console.print(Panel.fit(
                "[bold green]🎉 You're all caught up![/bold green]\n\n"
                "All your relationships are getting the attention they deserve!\n"
                "You're doing great! Keep it up! 💚",
                border_style="green"
            ))
            return

        # Sort by most overdue
        needs_attention.sort(key=lambda x: x["overdue"], reverse=True)

        console.print(Panel.fit(
            "[bold yellow]⏰ Connection Reminders[/bold yellow]\n\n"
            f"You have {len(needs_attention)} {'person' if len(needs_attention) == 1 else 'people'} "
            "who would love to hear from you!",
            border_style="yellow"
        ))

        for item in needs_attention:
            person = item["person"]
            console.print(
                f"\n[bold cyan]{person['name']}[/bold cyan] "
                f"({person['relationship_type']})\n"
                f"  Last contact: {item['days']} days ago\n"
                f"  Goal: Every {person['desired_frequency'].lower()}\n"
                f"  [yellow]⚠️  {item['overdue']} days overdue[/yellow]"
            )

        console.print(
            "\n[dim]💡 Tip: Even a quick text or call can make someone's day![/dim]"
        )

    def view_stats(self):
        """Display comprehensive statistics"""
        profile = self.data["profile"]

        # Level progress
        xp_needed = profile["level"] * 100
        xp_progress = profile["xp"]

        console.print(Panel.fit(
            f"[bold cyan]📊 Your Heartbeat Stats[/bold cyan]\n\n"
            f"[bold]Name:[/bold] {profile['name']}\n"
            f"[bold]Level:[/bold] {profile['level']} ⭐\n"
            f"[bold]XP:[/bold] {xp_progress}/{xp_needed}\n"
            f"[bold]Total Connections:[/bold] {profile['total_connections']} 💬\n"
            f"[bold]Acts of Kindness:[/bold] {profile['total_kindness_acts']} 🌟\n"
            f"[bold]People in Circle:[/bold] {len(self.data['relationships'])} 👥",
            border_style="cyan"
        ))

        # Relationship breakdown
        if self.data["relationships"]:
            console.print("\n[bold]Relationships by Type:[/bold]")
            type_counts = {}
            total_closeness = 0

            for person in self.data["relationships"].values():
                rel_type = person["relationship_type"]
                type_counts[rel_type] = type_counts.get(rel_type, 0) + 1
                total_closeness += person["closeness"]

            for rel_type, count in sorted(type_counts.items()):
                console.print(f"  {rel_type}: {count}")

            avg_closeness = total_closeness / len(self.data["relationships"])
            console.print(f"\n[bold]Average Closeness:[/bold] {avg_closeness:.1f}/10 ❤️")

        # Recent activity
        if self.data["interactions"]:
            recent = self.data["interactions"][-5:]
            console.print("\n[bold]Recent Interactions:[/bold]")
            for interaction in reversed(recent):
                date = datetime.fromisoformat(interaction["date"])
                console.print(
                    f"  • {interaction['person_name']} - {interaction['type']} "
                    f"({date.strftime('%b %d')})"
                )

        # Quality time
        total_quality_time = sum(
            p.get("quality_time_hours", 0)
            for p in self.data["relationships"].values()
        )
        console.print(f"\n[bold]Total Quality Time:[/bold] {total_quality_time:.1f} hours ⏰")

    def insights(self):
        """Provide insights about relationships"""
        if not self.data["relationships"]:
            console.print("[yellow]⚠️  Not enough data for insights yet.[/yellow]")
            return

        console.print(Panel.fit(
            "[bold cyan]💡 Relationship Insights[/bold cyan]",
            border_style="cyan"
        ))

        # Who you connect with most
        if self.data["interactions"]:
            person_interaction_count = {}
            for interaction in self.data["interactions"]:
                person_id = interaction["person_id"]
                person_interaction_count[person_id] = person_interaction_count.get(person_id, 0) + 1

            most_contacted_id = max(person_interaction_count, key=person_interaction_count.get)
            most_contacted = self.data["relationships"][most_contacted_id]

            console.print(
                f"\n[bold green]🏆 Most Connected With:[/bold green]\n"
                f"{most_contacted['name']} ({person_interaction_count[most_contacted_id]} interactions)"
            )

        # Highest quality interactions
        if self.data["interactions"]:
            high_quality = [i for i in self.data["interactions"] if i["quality"] >= 8]
            console.print(
                f"\n[bold yellow]⭐ High-Quality Connections:[/bold yellow]\n"
                f"{len(high_quality)} interactions rated 8+ out of 10"
            )

        # Closest relationships
        closest = sorted(
            self.data["relationships"].values(),
            key=lambda x: x["closeness"],
            reverse=True
        )[:3]

        console.print("\n[bold cyan]❤️  Your Closest Connections:[/bold cyan]")
        for person in closest:
            console.print(f"  {person['name']} - {person['closeness']}/10 {'❤️' * person['closeness']}")

        # Kindness impact
        if self.data["kindness_acts"]:
            total_impact = sum(k["impact"] for k in self.data["kindness_acts"])
            avg_impact = total_impact / len(self.data["kindness_acts"])

            console.print(
                f"\n[bold magenta]🌟 Kindness Impact:[/bold magenta]\n"
                f"Average impact: {avg_impact:.1f}/10\n"
                f"You're making a real difference! 💚"
            )

        # Connection consistency
        now = datetime.now()
        on_track = sum(
            1 for person in self.data["relationships"].values()
            if (now - datetime.fromisoformat(person["last_contact"])).days <= person["frequency_days"]
        )
        total = len(self.data["relationships"])
        consistency = (on_track / total) * 100

        console.print(
            f"\n[bold blue]📈 Connection Consistency:[/bold blue]\n"
            f"{on_track}/{total} relationships on track ({consistency:.0f}%)"
        )

        if consistency >= 80:
            console.print("[green]Excellent! You're very consistent! 🌟[/green]")
        elif consistency >= 60:
            console.print("[yellow]Good! Keep building those habits! 💪[/yellow]")
        else:
            console.print("[red]Room for improvement. Small efforts add up! 📈[/red]")

    def get_motivated(self):
        """Show motivational message"""
        import random

        quote = random.choice(RELATIONSHIP_QUOTES)

        console.print(Panel.fit(
            f"[bold cyan]💝 Motivation[/bold cyan]\n\n"
            f"[italic]{quote}[/italic]\n\n"
            "Remember: The relationships you nurture today\n"
            "become the support system you treasure tomorrow.\n\n"
            "[bold]Every connection matters. Every kind act ripples outward.[/bold]",
            border_style="cyan"
        ))

        # Personal encouragement based on stats
        if self.data["profile"]["total_connections"] >= 10:
            console.print("\n[green]You're building beautiful connections! Keep going! 🌟[/green]")
        elif self.data["profile"]["total_kindness_acts"] >= 5:
            console.print("\n[green]Your kindness is changing lives! Never stop! 💚[/green]")
        else:
            console.print("\n[cyan]Every journey starts with a single step. You're on your way! 🚀[/cyan]")

    def main_menu(self):
        """Display main menu and handle user choice"""
        while True:
            console.clear()

            profile = self.data["profile"]
            xp_needed = profile["level"] * 100
            xp_progress = profile["xp"]

            # Header with profile info
            console.print(Panel.fit(
                f"[bold red]❤️  Heartbeat - Nurture Your Connections  ❤️[/bold red]\n\n"
                f"[bold]{profile['name']}[/bold] | Level {profile['level']} | "
                f"XP: {xp_progress}/{xp_needed}\n"
                f"Connections: {profile['total_connections']} | "
                f"Kindness Acts: {profile['total_kindness_acts']}",
                border_style="red"
            ))

            # Menu options
            console.print("\n[bold cyan]Main Menu:[/bold cyan]\n")
            console.print("1. 👥 Add New Relationship")
            console.print("2. 💬 Log Interaction")
            console.print("3. 🌟 Log Act of Kindness")
            console.print("4. 📋 View All Relationships")
            console.print("5. ⏰ Connection Reminders")
            console.print("6. 📊 View Statistics")
            console.print("7. 💡 Insights & Analytics")
            console.print("8. 💝 Get Motivated")
            console.print("9. ❌ Exit")

            choice = Prompt.ask(
                "\n[bold]Choose an option[/bold]",
                choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            )

            if choice == "1":
                self.add_relationship()
            elif choice == "2":
                self.log_interaction()
            elif choice == "3":
                self.log_kindness()
            elif choice == "4":
                self.view_relationships()
            elif choice == "5":
                self.connection_reminders()
            elif choice == "6":
                self.view_stats()
            elif choice == "7":
                self.insights()
            elif choice == "8":
                self.get_motivated()
            elif choice == "9":
                console.print(Panel.fit(
                    "[bold green]Thank you for using Heartbeat! ❤️[/bold green]\n\n"
                    "Remember: A life rich in relationships\n"
                    "is a life rich in meaning.\n\n"
                    "Go nurture your connections! 🌟",
                    border_style="green"
                ))
                break

            if choice != "9":
                Prompt.ask("\n[dim]Press Enter to continue[/dim]")


def main():
    """Entry point"""
    try:
        app = HeartbeatApp()
        app.main_menu()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Goodbye! Take care of your relationships! ❤️[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        raise


if __name__ == "__main__":
    main()
