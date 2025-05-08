# 🎬 Netflix Content Analyzer

Ever wondered what makes a Netflix show different from a movie? This magical Python package helps you unveil the secrets behind streaming content using the power of machine learning! ✨

## 🔍 What's This All About?

Netflix Content Analyzer is your friendly neighborhood tool that dives deep into streaming content datasets (Netflix, Disney+, you name it!) to discover hidden patterns and cool insights. Here's what our digital detective can do:

- Clean up messy streaming data (because nobody likes a messy dataset!)
- Transform boring raw data into exciting machine learning features
- Build decision trees that predict whether content is a Movie or TV Show
- Create pretty visualizations that even your non-tech friends will understand
- Tell you how good our predictions actually are

## 🚀 Installation

```bash
# Clone the repository (fancy way of saying "download")
git clone https://github.com/yourusername/netflix-content-analyzer.git
cd netflix-content-analyzer

# Install the magic ingredients
pip install -r requirements.txt
```

## 🎮 How to Play

### Command Line Wizard

Fire up your terminal and cast this spell:

```bash
python main.py --input path/to/your/dataset.csv [--max_depth 3] [--output results/]
```

#### Required Magic Words:
- `--input`, `-i`: Where's your treasure map? (Path to your dataset CSV)

#### Optional Enchantments:
- `--max_depth`, `-d`: How deep down the rabbit hole? (Default: 3)
- `--output`, `-o`: Where to store your discovered secrets

### Example for the Impatient

```bash
python main.py --input data/netflix_titles.csv --max_depth 4 --output results/
```

### Using Our Magic in Your Own Spells

```python
import pandas as pd
from netflix_analyzer import analyze_netflix_content

# Load your super secret Netflix data
netflix_df = pd.read_csv("path/to/your/dataset.csv")

# Wave the magic wand
model, cleaned_data = analyze_netflix_content(netflix_df, max_depth=3)
```

## 📊 Dataset Ingredients

Your dataset should have these tasty columns (the more complete, the yummier the results!):
- `show_id`: A unique ID (like a social security number for your shows)
- `type`: Movie or TV Show (this is what we're trying to predict!)
- `title`: What's it called? ("Stranger Things", not "That Show with the Upside Down")
- `director`: Who called the shots?
- `cast`: The famous (or not-so-famous) people in it
- `country`: Where it was cooked up
- `date_added`: When Netflix decided to adopt it
- `release_year`: When it first said "hello world!"
- `rating`: PG, TV-MA, or "hide this from your parents"
- `duration`: How long it'll keep you on the couch ("90 min" or "5 Seasons of your life gone")
- `listed_in`: What genre shelf we'd find it on
- `description`: The "convince you to watch me" text

## 🌳 Machine Learning Magic Explained

This package uses **Decision Trees** - imagine a game of "20 Questions" but for classifying Netflix content:

1. **What's a Decision Tree?** It's like a flowchart your smart friend might make: "If duration > 100 minutes AND rating = 'R', then it's probably a Movie!"

2. The algorithm builds a tree of yes/no questions about your content's features, creating the ultimate "guess the content type" game.

3. ✨ Why Decision Trees are awesome for this:
   - You can actually SEE the decision-making process (no mysterious black boxes here!)
   - It tells you which features matter most (Is it duration? Release year? The fact it has "Part 2" in the title?)
   - Even your non-data-scientist friends can understand the results
   - Works great with all sorts of data - numbers, categories, you name it!

The model becomes a content detective, figuring out what separates a binge-worthy series from a movie night pick. You'll never look at Netflix the same way again!

## 🏰 Simple Example: Disney+ Content Analysis

Want to analyze the Mouse House instead? Use our simplified `DisneyMovie.py`:

```python
import pandas as pd
from DisneyMovie import analyze_netflix_content

# Load your Disney+ treasures
disney_df = pd.read_csv("path/to/disney_plus_titles.csv")

# Bibbidi-Bobbidi-Boo!
cleaned_data, analysis_results = analyze_netflix_content(disney_df)
```

## 🧙‍♂️ Dependencies

Our magic potion requires:
- Python 3.7+ (the cauldron)
- pandas (for wrangling data dragons)
- numpy (for mathematical spells)
- scikit-learn (where the ML wizardry happens)
- matplotlib & seaborn (to make pretty pictures)
