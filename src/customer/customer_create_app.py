import customer_cmd
import customer
import repository
import logging

logger = logging.getLogger(__name__)

def regist_customer(cstr_cmd:customer_cmd) -> str:

    entity = customer.Customer(cstr_cmd)

    try:
        conn = repository.getConnection()
        repository.save(entity,conn)
        conn.commit()
    except Exception as e:
        logger.error("error : %s",e)
        conn.rollback()
        raise Exception('database access error')
    finally:
        conn.close()

    return entity.get_id()
