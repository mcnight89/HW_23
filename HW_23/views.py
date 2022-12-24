from flask import Blueprint, request, jsonify

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)

FILE_NAME = '/home/pavel/PycharmProjects/HW_23/data/apache_logs.txt'  # 'data/apache_logs.txt'
""" Написал абсолютный путь т.к.  на Ubuntu по другому не работало """


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json

    validated_data = BatchRequestSchema().load(data)
    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result,
        )
    return jsonify(result)
