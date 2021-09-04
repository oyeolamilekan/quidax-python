from quidaxapi.base import QuidaxBase


class Quotes(QuidaxBase):

    @classmethod
    def quote(cls, market, unit, kind, volume):
        return cls().requests.get(f'quotes?market={market}&unit={unit}&kind={kind}&volume={volume}')
