# Phishing-Website-Detection-using-Machine-Learning-PhishGuard-
PhishGuard is a machine learning–based phishing detection system designed to identify malicious URLs using feature engineering and classification techniques. The system analyzes structural patterns in URLs and predicts whether a link is legitimate or phishing with a confidence score. 
Features:
1. URL-based phishing detection
2. Machine Learning model using Random Forest Classifier
3. Feature extraction from URLs (8 key parameters)
4. Real-time scanning of URLs
5. Model evaluation using accuracy & classification report
 Optimized for common Indian phishing patterns (KYC, banking scams, etc.)
6. Feature Engineering

The system extracts the following features from each URL:

URL Length (len)
Presence of @ symbol (at_key)
Number of // (slashes)
IP address usage (is_ip)
Hyphen count (hyphens)
Fake HTTPS detection (fake_ssl)
Dot count (dots)
Suspicious keywords (bad_words)
Tech Stack
Python 
Pandas & NumPy
Scikit-learn (Random Forest)
Regex (re) for pattern matching

How It Works:
Raw URL dataset is provided (legitimate and as well as phishing).
URLs are converted into numerical feature vectors.
Dataset is split into training and testing sets.
Random Forest model is trained on the data.
Model performance is evaluated using accuracy and classification report.
New URLs can be scanned in real time.
Model Performance
Uses 125 estimators for better accuracy
Achieves high accuracy on test dataset
Outputs:
Prediction (Legitimate / Phishing)
Confidence score

Example Output
[Scanning] https://www.google.co.in/
Result -> OK: LEGITIMATE (98.45%)

[Scanning] http://bit.ly/paytm-kyc-update-now
Result -> !!! DANGER: PHISHING !!! (96.72%)



Project Structure
PhishGuard__
phishguard.py
README.md
requirements.txt


How to Run:
Clone the repository
git clone https://github.com/your-username/phishguard.git
Install dependencies
pip install pandas numpy scikit-learn
Run the script
python phishguard.py

 Future Improvements
 Integration with browser extension
 Real-time API for phishing detection
 Deep Learning model for higher accuracy
 Larger dataset for training
 Integration with threat intelligence feeds


Authors-
Raghvendra Kumar Singh
Shubham Yadav



