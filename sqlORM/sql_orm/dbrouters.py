from sql_orm.models import Wizard


class Sql_ormDBRouter:
    def db_for_read(self, model, **hints):
        if model == Wizard:
            return 'mysql'
        return None

    def db_for_write(self, model, **hints):
        if model == Wizard:
            return 'mysql'
        return None
