import os

import click

import magic

from strava import api
from strava.decorators import login_required, format_result


_COLUMNS = (
    'id',
    'external_id',
    'activity_id',
    'error',
    'status'
)


@click.command('upload')
@click.argument('filename', type=click.Path(exists=True, dir_okay=False))
@click.option('--data-type', type=click.Choice(('fit','fit.gz','tcx','tcx.gz','gpx','gpx.gz')))
@login_required
@format_result(table_columns=_COLUMNS, single=True)
def post_upload(filename, data_type=None):
    # if no data_type is provided, try to guess it from the filename
    #
    # python-magic can identify gzip and FIT files.
    # TCX and GPX are XML and need additional guessing.
    if not data_type:
        magic_type = magic.from_file(filename).split(',')[0]
        gz = magic_type == 'gzip compressed data'
        if gz:
            magic_type = magic.Magic(uncompress=True).from_file(filename).split(',')[0]

        if magic_type == 'FIT Map data':
            data_type = 'fit'
        elif magic_type == 'XML 1.0 document':
            guess = filename.split('.')[-2 if gz else -1].lower()
            if guess in ('tcx', 'gpx'):
                data_type = guess

        if data_type and gz:
            data_type += '.gz'

    # if there's still no data_type, error out
    if not data_type:
        click.echo('Failed to guess data file type, please specify with --data-type.')
        exit(1)

    return api.post_uploads(filename, data_type)


@click.command('upload-status')
@click.argument('upload_id', nargs=-1, required=True)
@login_required
@format_result(table_columns=_COLUMNS)
def get_upload(upload_id):
    return [api.get_uploads(id_) for id_ in upload_id]
