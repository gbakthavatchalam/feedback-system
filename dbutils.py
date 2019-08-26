from settings import session


async def save(_object):
    session.add(_object)
    session.commit()
    return _object


