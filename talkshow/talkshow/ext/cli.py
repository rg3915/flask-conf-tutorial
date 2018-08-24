import click


def configure(app):
    ''' Attach new commands in to app. '''
    @app.cli.command()
    @click.option('--name', '-n', required=True)
    @click.option('--date', '-d', required=True)
    def addevent(name, date):
        ''' Creates a new event entry. '''
        event = app.db['events'].insert_one({'name': name, 'date': date})
        # click.echo(f'Name: {name} Date: {date}')
        click.echo(f"{event.inserted_id} cadastrado com sucesso!")
