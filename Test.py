from cerebras_unofficial import Cerebras

if __name__ == "__main__":
    ai = Cerebras('cookieyes-consent=consentid:U1xxxxx')
    response = ai.generate("what is Thermodynamics?")
    print(f"Response: {response}")

    ai = Cerebras('csk-cytxxxxx')
    response = ai.generate("what is Thermodynamics?")
    print(f"Response: {response}")
