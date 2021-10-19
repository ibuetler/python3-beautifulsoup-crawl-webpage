# Crawling Projkect
## Installation
```
pipenv --python 3 shell
pipenv sync
python crawl_email.py
```

## Results
* script will generate file `emails.csv`


## Crawl BFH
* email not obfuscated
* crawling directly possible
* crawl_email_bfh.py

## Crawl Swisswine
* email obfuscated with java-script (CloudFlare email protection)
* crawling of e-mails not directly possible
* it is still possible, but java script must be executed, otherwise not seen in source code
* solution available too, but not part of this repo
* e1@hacking-lab.com


