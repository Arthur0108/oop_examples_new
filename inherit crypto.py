class Crypto:

    def __init__(self, name, capitalization):
        self.name = name
        self.capitalization = capitalization
        print(f'We like {self.name}!')

    def info(self):
        print(f'We have crypto: {self.name}, capitalization: {self.capitalization}, ', end=' ')


class Ethereum(Crypto):
    def __init__(self, name, capitalization, nft):
        Crypto.__init__(self, name, capitalization)
        self.nft = nft
        print(f'We bought {self.name} on the Craken exchange.')

    def info(self):
        Crypto.info(self)
        print(f'we can create {self.nft} on ethereum.')


class Cardano(Crypto):
    def __init__(self, name, capitalization, staking):
        Crypto.__init__(self, name, capitalization)
        self.staking = staking
        print(f'We bought {self.name} on the Cuna exchange.')

    def info(self):
        Crypto.info(self)
        print(f'Staking Cardano is {self.staking}.')


class Bitcoin(Crypto):
    def __init__(self, name, capitalization, asic_mining):
        Crypto.__init__(self, name, capitalization)
        self.asic_mining = asic_mining
        print(f'We bought {self.name} on the Binance exchange.')

    def info(self):
        Crypto.info(self)
        print(f'Best for Bitcoin mining is {self.asic_mining}.')


e = Ethereum('Ethereum', '13 trillion', 'Best NFT')
c = Cardano('Cardano Ada', '1 trillion', '5% per annum')
b = Bitcoin('Bitcoin', '30 trillion', 'Antminer S19 PRO')
print()

best_crypto = [e, c, b]
for best in best_crypto:
    best.info()
