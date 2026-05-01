import re
import math
import logging
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
logging.basicConfig(level=logging.INFO, format='%(message)s')
class ThreatSentryML:
    def __init__(self, datasource='urls.csv'):
        self.brain = RandomForestClassifier(n_estimators=210, criterion='entropy', max_depth=18, random_state=88)
        self.datasource = datasource
        self.indicators = ['length', 'entropy', 'delim_qty', 'is_raw_ip', 'hyphenation', 'fake_protocol', 'dot_ratio', 'trigger_weight']
        self.keywords = {'login', 'verify', 'update', 'kyc', 'secure', 'refund', 'win', 'claim', 'bill', 'bank'}
        self.initialized = False
    def _get_shannon_entropy(self, data):
        if not data: return 0
        freqs = Counter(data)
        probs = [f/len(data) for f in freqs.values()]
        return -sum(p * math.log(p, 2) for p in probs)
    def _extract_lexical_dna(self, url):
        url = str(url).lower().strip()
        netloc = url.split('://')[-1]
        h_val = self._get_shannon_entropy(url)
        is_ip = 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0
        spoof = 1 if "https" in netloc and not url.startswith("https") else 0
        hits = 1 if any(k in url for k in self.keywords) else 0
        dots = url.count('.') / len(url) if len(url) > 0 else 0
        return [len(url), h_val, url.count('/'), is_ip, url.count('-'), spoof, dots, hits]
    def sync_engine(self):
        try:
            df_raw = pd.read_csv(self.datasource)
            X = [self._extract_lexical_dna(u) for u in df_raw['url']]
            y = df_raw['label'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.18, random_state=88)
            self.brain.fit(X_train, y_train)
            self.initialized = True
            return self.brain.score(X_test, y_test)
        except FileNotFoundError:
            return None
    def evaluate(self, target_url):
        if not self.initialized: self.sync_engine()
        vector = np.array(self._extract_lexical_dna(target_url)).reshape(1, -1)
        prediction = self.brain.predict(vector)[0]
        confidence = self.brain.predict_proba(vector)[0][prediction]
        return "MALICIOUS" if prediction == 1 else "LEGITIMATE", confidence
if __name__ == "__main__":
    sentry = ThreatSentryML()
    accuracy = sentry.sync_engine()
    if accuracy:
        print(f"Engine Ready. Precision: {accuracy:.2%}")
        test_link = input("Target URL: ")
        res, conf = sentry.evaluate(test_link)
        print(f"Result: {res} [{conf:.2%}]")

import pandas as pd
data = {
    'url': [
        "https://www.onlinesbi.sbi/portal/", "https://www.irctc.co.in/",
        "http://103.45.122.1/sbi-login/", "http://bit.ly/paytm-kyc-now",
        "https://uidai.gov.in/", "http://electricity-bill-pay.org",
        "https://www.amazon.in/", "http://amazon-lucky-draw.net"
    ] * 15, 
    'label': [0, 0, 1, 1, 0, 1, 0, 1] * 15
}
pd.DataFrame(data).to_csv('urls.csv', index=False)
print("File 'urls.csv' created successfully!")
