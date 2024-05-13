gpg --quiet --batch --yes --decrypt --passphrase=$GOOGLE_API_PW \
        --output $GITHUB_WORKSPACE/django_project/credentials.json $GITHUB_WORKSPACE/django_project/credentials.json.gpg