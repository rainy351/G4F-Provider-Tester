import g4f

provider_names = g4f.Provider.__all__

failed_providers = []

for provider_name in provider_names:
    provider = getattr(g4f.Provider, provider_name)
    if provider.working:
        try:
            string =""
            provider = getattr(g4f.Provider, provider_name)
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "How are you?"}],
                stream=False,
                provider=provider
            )
            if response:
                print(f"{provider_name}: {response}")
                
        except Exception as e:
            failed_providers.append(f"{provider_name}: {e}")

print("\n\n\n\n\nFAILED PROVIDERS:\n\n")
for failed_provider in failed_providers:
    print(failed_provider)
