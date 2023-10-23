import OpenAI from 'openai';

/*
const configuration = new Configuration({
    organization: "org-vkVVSns03Fg7ueAEGNBoaXva",
    apiKey: "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",
});

const openai = new OpenAIApi(configuration);
*/

const openai = new OpenAI({
    organization: "org-vkVVSns03Fg7ueAEGNBoaXva",
    apiKey: "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",
  });

const completion = await openai.chat.completions.create({
    model: "gpt-4",
    messages: [
        {role: "user", content: "Hello, how are you?"}
    ]
});

console.log(completion.choices[0].message);

//https://openai.com/pricing
//gpt-3.5-turbo