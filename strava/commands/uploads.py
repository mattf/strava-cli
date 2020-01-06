import os

import click

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
@login_required
@format_result(table_columns=_COLUMNS, single=True)
def post_upload(filename, data_type="fit"):
    return api.post_uploads(filename, data_type)


@click.command('upload-status')
@click.argument('upload_id', nargs=-1, required=True)
@login_required
@format_result(table_columns=_COLUMNS)
def get_upload(upload_id):
    return [api.get_uploads(id_) for id_ in upload_id]
