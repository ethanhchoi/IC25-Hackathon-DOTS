import OpenAI from "openai";
import http from "http";


const server = http.createServer((req,res) => {
    
        res.setHeader('Access-Control-Allow-Origin','*');
        res.writeHead(200, {'Content-Type':'text/plain'});

        let body = '';

        // Collect data chunks as they arrive

        req.on('data', chunk => {
            body += chunk;
        });

        req.on('end', async () => {
            res = await AiQuery(body)
            res.end(JSON.stringify(res))
        });

    }).listen(3000,() => {
        console.log("server started\n");
    });


async function AiQuery(query){
    const openai = new OpenAI({ apiKey: 'API-KEY' });
    const completion = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [
            { role: "system", content: "You are a helpful assistant." },
            {
                role: "user",
                content: query,
            },
        ],
        store: true,
    });
    //gets the response of the prompt
    return completion.choices[0].message.content;
}