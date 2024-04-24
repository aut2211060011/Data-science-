import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load hotel booking data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(data):
    """Clean the hotel booking data by removing missing values."""
    return data.dropna()

def analyze_data(data):
    """Analyze the hotel booking data."""
    # Summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Visualize booking distribution by hotel type
    sns.countplot(x='hotel', data=data)
    plt.title('Booking Distribution by Hotel Type')
    plt.show()

    # Correlation matrix
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.title('Correlation Matrix')
    plt.show()

    # Analyze booking distribution by country
    sns.countplot(x='country', data=data)
    plt.title('Booking Distribution by Country')
    plt.xticks(rotation=45)
    plt.show()

def main():
    # Load data
    file_path = 'hotel_bookings.csv'
    hotel_data = load_data(file_path)

    # Clean data
    hotel_data_cleaned = clean_data(hotel_data)

    # Analyze data
    analyze_data(hotel_data_cleaned)

if __name__ == "__main__":
    main()

    
