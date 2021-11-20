# junction-miro-task-2021

This is the github repository for a Junction 2021 project. \
This task is for the company Miro \
### The problem we are solving
We are solving the problem of tranferring words from a physical source into the Miro whiteboard using optical character recognition (OCR) \
### Technical part
We use the miro platform in our solution
The user sends a photo to a Telegram Bot made with Telegram API. The photo is then sent to a cloud service made with Google Cloud API where a Pytorch OCR framework processes the photo and pulls text out of it. Then the text is written into the miro whiteboard. The Rest API of miro, as of time of writing, doesn't let us create an app that can send photos, however we can write text with it, for this reason the request must be sent using Telegram API and the return text written into the miro whiteboard will be done using Rest API. \
### Impact on the user
Users using this app will spend much less time and be more happy. Writing out word for word is very tedious and takes a long time which leads to unhappiness, by using our faster method, you can do tasks of transferring from paper into the internet much faster and not be unhappy!


