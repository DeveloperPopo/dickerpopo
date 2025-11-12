# ✨ Momentum - Transform Your Life, One Day at a Time

**Momentum** is a comprehensive personal development CLI tool designed to genuinely transform your daily life. It's not just another productivity app—it's your personal life transformation system that combines goal tracking, habit building, journaling, mood tracking, and gamification into one beautiful, easy-to-use command-line interface.

## 🌟 Why Momentum is Life-Changing

1. **Holistic Self-Improvement** - Track every aspect of your personal growth in one place
2. **Beautiful & Motivating** - Gorgeous terminal UI with progress bars, tables, and celebratory messages
3. **Gamification** - Level up, earn XP, and unlock badges as you improve your life
4. **Daily Rituals** - Morning intentions and evening reflections to bookend your day mindfully
5. **Habit Streaks** - Build powerful habits with streak tracking and visual feedback
6. **Goal Achievement** - Set, track, and complete meaningful goals with progress visualization
7. **Mood Insights** - Understand your emotional patterns and energy levels over time
8. **Private & Secure** - All data stored locally on your machine in `~/.momentum/data.json`

## 🚀 Features

### 📋 Daily Check-ins
- **Morning Intentions**: Set your top 3 intentions, practice gratitude, and rate your energy
- **Evening Reflections**: Review wins, lessons learned, and areas for improvement
- Build mindful awareness of your daily experience

### 🎯 Goal Management
- Create SMART goals across multiple categories (health, career, finance, learning, etc.)
- Track progress with beautiful visual progress bars
- Set deadlines and get satisfaction from completing goals
- Earn bonus XP for goal completion

### ⚡ Habit Tracker
- Build positive habits with daily, weekly, or custom frequencies
- Track current and best streaks with 🔥 fire indicators
- Get motivated by seeing your consistency grow
- Earn XP for each habit completion

### 📝 Journaling
- Free-form journaling for self-expression
- Automatic timestamping and organization
- Review recent entries to reflect on your journey

### 😊 Mood & Energy Tracking
- Log your mood, energy level, and stress
- Add optional notes about what's affecting your wellbeing
- View trends to understand what influences your mental state

### 📊 Progress & Analytics
- View comprehensive statistics about your journey
- See total goals completed, habits tracked, and journal entries
- Track your level and XP progress
- Get insights about habit streaks and goal progress

### 🏆 Gamification System
- **Level System**: Earn XP and level up as you complete actions
- **XP Rewards**:
  - Daily check-ins: 10 XP
  - Journal entries: 10 XP
  - Mood tracking: 5 XP
  - New goal/habit: 15-20 XP
  - Habit completion: 15 XP
  - Goal completion: 50 XP
  - Goal progress updates: 10-30 XP
- **Level Up**: Every 100 XP per level (Level 2 = 200 XP, Level 3 = 300 XP, etc.)

### 🌟 Daily Motivation
- Inspirational quotes from great thinkers
- Encouraging messages tailored to your progress
- Celebration panels for achievements and milestones

## 📦 Installation

### Option 1: Quick Start (Recommended)

```bash
# Clone or download the repository
git clone https://github.com/DeveloperPopo/dickerpopo.git
cd dickerpopo

# Install dependencies (automatically handled on first run, or manually):
pip install -r requirements.txt

# Make executable (Linux/Mac)
chmod +x momentum.py

# Run it!
python3 momentum.py

# Or if you made it executable:
./momentum.py
```

### Option 2: Install Globally

```bash
# Create a symlink to run from anywhere (Linux/Mac)
sudo ln -s $(pwd)/momentum.py /usr/local/bin/momentum

# Now you can run it from anywhere:
momentum
```

### Option 3: Python Installation

```bash
# Just make sure you have Python 3.7+ and run:
pip install rich
python3 momentum.py
```

## 🎮 How to Use

### First Time Setup

When you first run Momentum, it will:
1. Create a data directory at `~/.momentum/`
2. Initialize your data file with default values
3. Show you the main menu with all available options

### Main Menu Options

1. **📋 Daily Check-in** - Start your morning or close your evening
2. **🎯 Manage Goals** - Create, update, and complete goals
3. **⚡ Manage Habits** - Add habits and track daily completion
4. **📝 Journal Entry** - Write or read journal entries
5. **😊 Track Mood & Energy** - Log how you're feeling
6. **📊 View Progress** - See your statistics and achievements
7. **💡 Insights & Analytics** - Get insights about your patterns
8. **🌟 Get Motivated** - Receive inspirational messages

### Recommended Daily Routine

**Morning (5 minutes)**:
1. Open Momentum: `python3 momentum.py`
2. Choose option 1: Daily Check-in → Morning
3. Set your 3 intentions for the day
4. Express gratitude
5. Rate your energy level
6. Review your active goals and habits

**Throughout the Day**:
- Log habits as you complete them (option 3 → 2)
- Update goal progress when you make progress (option 2 → 2)
- Journal when inspiration strikes (option 4)

**Evening (5 minutes)**:
1. Choose option 1: Daily Check-in → Evening
2. Reflect on your wins
3. Note what you learned
4. Identify one thing to improve tomorrow
5. Rate your overall day
6. Check your progress and celebrate achievements!

### Pro Tips

1. **Be Consistent**: Use Momentum every day, even if just for check-ins
2. **Start Small**: Don't create 20 goals on day 1. Start with 2-3 meaningful ones
3. **Celebrate Wins**: Take time to appreciate when you complete goals or hit streaks
4. **Review Insights**: Check your analytics weekly to spot patterns
5. **Be Honest**: The more authentic your entries, the more valuable your data
6. **Don't Break the Chain**: Focus on building habit streaks—they're powerful!

## 🎯 Example Use Cases

### Career Development
- **Goal**: "Get promoted to Senior Developer" (target: 100%)
- **Habits**: "Code for 1 hour daily", "Read tech articles", "Network on LinkedIn"
- **Track**: Mood before/after work, energy levels
- **Journal**: Document learnings, challenges, victories

### Health & Fitness
- **Goals**: "Lose 20 pounds", "Run 5K in under 30 minutes"
- **Habits**: "Morning workout", "Drink 8 glasses of water", "10,000 steps"
- **Track**: Energy levels, mood correlation with exercise
- **Journal**: How different foods make you feel

### Personal Growth
- **Goals**: "Read 24 books this year", "Learn Spanish (B2 level)"
- **Habits**: "Meditate 10 minutes", "Read for 30 minutes", "Practice Spanish"
- **Track**: Stress levels, emotional patterns
- **Journal**: Insights from books, personal reflections

### Financial Goals
- **Goals**: "Save $10,000", "Pay off credit card debt"
- **Habits**: "Review spending daily", "No impulse purchases", "Side hustle 1 hour"
- **Track**: Stress related to finances
- **Journal**: Money mindset reflections

## 📊 Data & Privacy

- **All data is stored locally** in `~/.momentum/data.json`
- **No internet connection required** - works 100% offline
- **No tracking, no analytics, no cloud sync** - your data stays yours
- **Easy to backup** - just copy the `~/.momentum` folder
- **Human-readable format** - JSON file you can inspect anytime

## 🎨 Screenshots

When you run Momentum, you'll see:
- Beautiful bordered panels with colors and emojis
- Progress bars showing goal completion
- Tables displaying your habits and streaks
- Level up celebrations with ASCII art
- Inspirational quotes to start your day
- Statistics and insights about your journey

## 🔧 Technical Details

- **Language**: Python 3.7+
- **Dependencies**: Rich (for beautiful terminal UI)
- **Data Storage**: JSON file at `~/.momentum/data.json`
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Size**: Lightweight (~30KB for the script)

## 🛠️ Troubleshooting

### "rich module not found"
```bash
pip install rich
```

### "Permission denied"
```bash
chmod +x momentum.py
```

### "Data not saving"
Check that `~/.momentum/` directory is writable:
```bash
ls -la ~/.momentum/
```

### Start Fresh
To reset all data:
```bash
rm -rf ~/.momentum/
```

## 🌱 Philosophy

Momentum is built on these principles:

1. **Small Daily Actions** - Massive long-term results come from tiny consistent steps
2. **Awareness** - You can't improve what you don't measure
3. **Celebration** - Acknowledging wins fuels motivation
4. **Reflection** - Learning from experience accelerates growth
5. **Simplicity** - A tool should enhance life, not complicate it
6. **Privacy** - Your personal growth data should stay personal

## 🚀 Future Enhancements (Potential)

Ideas for future versions:
- Export data to CSV/PDF for deeper analysis
- Habit correlation with mood (which habits boost your mood most?)
- Weekly/monthly review summaries
- Custom badges and achievements
- Goal templates for common objectives
- Data visualization with charts
- Backup/restore functionality
- Multiple user profiles
- Integration with calendar apps
- Mobile companion app

## 🤝 Contributing

This is an open-source project! Feel free to:
- Report bugs or request features via GitHub issues
- Fork and submit pull requests
- Share your success stories
- Suggest new features or improvements

## 📄 License

MIT License - see LICENSE file for details.

Feel free to use, modify, and distribute this tool. If it changes your life, pay it forward by helping others! 💚

## 💬 Final Thoughts

**Momentum** isn't just a tool—it's a commitment to yourself. Every time you open it, you're saying "I matter. My growth matters. My future matters."

Small daily improvements compound into life-changing results. This tool helps you stay accountable, build momentum (hence the name!), and create the life you've always wanted.

Start today. Your future self will thank you. 🚀

---

Made with ❤️ for everyone who wants to become the best version of themselves.

**Remember**: You're not competing with others. You're competing with who you were yesterday.

Now go build some momentum! ⚡
