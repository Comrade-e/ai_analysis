import g4f
import asyncio
client = g4f.client.Client()
async def ask(word, marker):
    c = True
    r = None
    while c:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f'Напишите только 1 или 0. Подходит ли слово или словосочетание "{word}" по контексту, окраске и смысловой связи к слову "{marker}". Напишите 1, если да, и 0, если нет'}]
            )
        try:
            r = int(response.choices[0].message.content)
            c = False
        except Exception as e:
            print(e)
    return r

def ask_sync(word, marker):
    c = True
    r = None
    while c:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f'Напишите только 1 или 0. Подходит ли слово или словосочетание "{word}" по контексту, окраске и смысловой связи к слову "{marker}". Напишите 1, если да, и 0, если нет'}]
            )
        try:
            r = int(response.choices[0].message.content)
            c = False
        except Exception as e:
            print(e)
    return r

if __name__ == '__main__':
    async def main():
        x = await ask('лагает', 'не понравилось')
        print(x)
    asyncio.run(main())