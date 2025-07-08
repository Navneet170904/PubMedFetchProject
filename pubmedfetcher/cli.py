import typer
from .fetcher import fetch_pubmed_papers

app = typer.Typer()

@app.command()
def main(
    query: str,
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output"),
    file: str = typer.Option(None, "--file", "-f", help="CSV output file")
):
    """
    Fetch PubMed papers based on a query and output results.
    """
    df = fetch_pubmed_papers(query, debug=debug)
    if file:
        df.to_csv(file, index=False)
        typer.echo(f"✅ Results saved to {file}")
    else:
        typer.echo(df.to_string(index=False))

if __name__ == "__main__":
    app()
