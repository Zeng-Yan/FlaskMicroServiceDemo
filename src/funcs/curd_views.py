# cython: language_level=3

from flask import request, jsonify, Response
from flask import current_app as app
from sqlalchemy import text, inspect

from src.database import tables
from src.database.exts import db
from src.configs import STATUS_CODE

TABLE_AFFINE = {
    tables.Point.__tablename__: tables.Point,
    tables.Target.__tablename__: tables.Target,
}


@app.route(f'/db/<root>/query_all', methods=['GET'])
def query_all(root: str) -> Response:
    """
    A universal function for querying all records in a table identified by $root,
    and return the result in json format. 
    Optionally, passing $order_by to specify a key for ordering query result,
    and $sort_by for indicating sorting order, value [descend] for descending as well as others for ascending.
        :return: JSON Response like {status: status code, result: {index: {key: value}}}
    """
    table = TABLE_AFFINE[root]
    order_key = request.values.get('order_by')

    try:
        if order_key:
            sort_order = f'-{order_key}' if request.values.get('sort_by') == 'descend' else f'+{order_key}'
            res = table.query.order_by(text(sort_order)).all()
        else:
            res = table.query.all()
        result = {str(idx): record.serialize() for idx, record in enumerate(res)}
    except Exception as error:
        response = {
            'status': STATUS_CODE['error'],
            'info': f'[ERROR] Failing to query all in {root} '
                    f'from {request.headers}: \n\t{error}',
            'result': None,
            }
    else:
        response = {
            'status': STATUS_CODE['success'],
            'info': f'[INFO] Successfully query all in {root} '
                    f'from {request.headers}',
            'result': result, 
            }
    print(response['info'])
    return jsonify(response)


@app.route(f'/db/<root>/query_by_key', methods=['GET'])
def query_by_key(root: str) -> Response:
    """
    A universal function for querying a record by $key and $value in a table identified by $root,
    and return the result in json format if the record is existed, otherwise return None.
        :return: JSON Response like {status: status code, result: {key: value}}
    """
    table = TABLE_AFFINE[root]
    key, value = request.values['key'], request.values['value']

    try:
        query_record = table.query.filter_by(**{key: value})  # ??????????????????????????????record
        result = {str(idx): r.serialize() for idx, r in enumerate(query_record)}
    except Exception as error:
        print(error)
        response = {
            'status': STATUS_CODE['error'],
            'info': f'[ERROR] Failing to query in {root} '
                    f'with key={key} value={value} from {request.headers}: \n\t{error}',
            'result': None,
            }
    else:
        response = {
            'status': STATUS_CODE['success'],
            'info': f'[INFO] Successfully query in {root} '
                    f'with key={key} value={value} from {request.headers}',
            'result': result, 
            }
    print(response['info'])
    return jsonify(response)


@app.route(f'/db/<root>/insert', methods=['GET'])
def insert(root: str) -> Response:
    """
    A universal function for inserting a record into a table identified by $root, 
    and return the operation status.
    [NOTE] modifying this function with method 'POST' is recommended.
        :return: JSON Response like {status: status code, info: info string}
    """
    table = TABLE_AFFINE[root]
    record = {k: request.values[k] for k in request.values.keys()}
    record = table(**record)  # ???????????????????????????
    primary_key = inspect(table).primary_key[0].name

    try:
        db.session.add(record)  # ???????????????
        # db.session.flush()
        # record_ = record.serialize()
        db.session.commit()  # ??????
    except Exception as error:
        response = {
            'status': STATUS_CODE['error'],
            'info': f'[ERROR] Failing to insert in {root} '
                    f'with key={primary_key} value={record[primary_key]} from {request.headers}: \n\t{error}',
            }
    else:
        response = {
            'status': STATUS_CODE['success'],
            'info': f'[INFO] Successfully insert in {root} '
                    f'with key={primary_key} value={record[primary_key]} from {request.headers}',
            }
    print(response['info'])
    return jsonify(response)


@app.route(f'/db/<root>/update_by_key')
def update_by_key(root: str) -> Response:
    """
    A universal function for updating a record by $key and $value in a table identified by $root, 
    and return the operation status.
    [NOTE] modifying this function with method 'POST' is recommended.
        :return: JSON Response like {status: status code, info: info string}
    """
    key, value = request.values['key'], request.values['value']
    table = TABLE_AFFINE[root]

    record = {k: request.values[k] for k in request.values.keys() if k not in ('key', 'value')}

    try:
        table.query.filter_by(**{key: value}).update(record)     
        db.session.commit()
    # except AttributeError as e:
    #     return '[ERROR] update failed: no id matched.', STATUS_CODE['error']
    except Exception as error:
        response = {
            'status': STATUS_CODE['error'],
            'info': f'[ERROR] Failing to update in {root} '
                    f'with key={key} value={value} from {request.headers}: \n\t{error}',
            }
    else:
        response = {
            'status': STATUS_CODE['success'],
            'info': f'[INFO] Successfully update in {root} '
                    f'with key={key} value={value} from {request.headers}',
            }
    print(response['info'])
    return jsonify(response)


@app.route(f'/db/<root>/drop_by_key')
def drop_by_key(root: str) -> Response:
    """
    A universal function for dropping a record by $key and $value in a table identified by $root, 
    and return the operation status.
        :return: JSON Response like {status: status code, info: info string}
    """
    key, value = request.values['key'], request.values['value']
    table = TABLE_AFFINE[root]

    try:
        table.query.filter_by(**{key: value}).delete()
        db.session.commit()
    # except AttributeError as e:
    #     return '[ERROR] delete failed: no id matched.', STATUS_CODE['error']
    except Exception as error:
        response = {
            'status': STATUS_CODE['error'], 
            'info': f'[ERROR] Failing to drop in {root} '
                    f'with key={key} value={value} from {request.headers}: \n\t{error}',
            }
    else:
        response = {
            'status': STATUS_CODE['success'],
            'info': f'[INFO] Successfully drop in {root} '
                    f'with key={key} value={value} from {request.headers}',
            }
    print(response['info'])
    return jsonify(response)
