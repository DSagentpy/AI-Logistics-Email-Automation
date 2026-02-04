import os.path
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def autenticar():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def buscar_emails_remetente(remetente):
    creds = autenticar()
    service = build('gmail', 'v1', credentials=creds)

    query = f'from:{remetente}'

    resultado = service.users().messages().list(
        userId='me',
        q=query,
        maxResults=10
    ).execute()

    mensagens = resultado.get('messages', [])

    corpos = []

    for msg in mensagens:
        txt = service.users().messages().get(
            userId='me', id=msg['id'], format='full').execute()

        payload = txt['payload']

        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body']['data']
                    texto = base64.urlsafe_b64decode(data).decode()
                    corpos.append(texto)

    return corpos