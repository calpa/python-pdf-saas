FROM gitpod/workspace-full

RUN curl -fsSL https://get.deta.dev/cli.sh | sh

RUN source ~/.bashrc

RUN pip3 install -r requirements.txt

CMD uvicorn main:app --reload