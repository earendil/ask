import requests
import click


@click.command()
@click.option("-s", "--subject", default="python")
@click.argument('question', nargs=-1)
def main(subject, question):
    sanitizedString = "+".join(question)
    print requests.get("http://cht.sh/{}/{}".format(subject, sanitizedString)).content


if __name__ == "__main__":
    main()
