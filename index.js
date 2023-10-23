import { Configuration, OpenAIApi } from 'openai';

const configuration = new Configuration({
    organization: "org-vkVVSns03Fg7ueAEGNBoaXva",
    apiKey: "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",
});

const openai = new OpenAIApi(configuration);

const completion = await openai.createChatCompletion({
    model: "gpt-4",
    messages: [
        {role: "user", content: "Hello, how are you?"}
    ]
});

console.log(completion.data.choices[0].message);