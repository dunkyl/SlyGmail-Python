import sys, pytest, os
from SlyGmail import *

test_dir = os.path.dirname(__file__)

@pytest.mark.skipif(sys.gettrace() is None, reason="sends real email")
async def test_readme():

    gmail = Gmail(OAuth2(F'{test_dir}/app.json', F'{test_dir}/user.json'))

    to_email = open(F'{test_dir}/test_email.txt').read().strip()

    await gmail.send(to_email, F'{test_dir} subject', F'{test_dir} body')

@pytest.mark.skipif(sys.gettrace() is None, reason="sends real email")
async def test_send_attachment():

    gmail = Gmail(OAuth2(F'{test_dir}/app.json', F'{test_dir}/user.json'))

    to_email = open(F'{test_dir}/test_email.txt').read().strip()

    await gmail.send(to_email, 'My Subject Unto You',
        """
            Hi there,

            Please see the attached test file.

            Thanks,
            Me
        """, [F'{test_dir}/test_attachment.txt'])