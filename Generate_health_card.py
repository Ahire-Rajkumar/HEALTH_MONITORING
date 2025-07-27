from PIL import ImageFont, ImageDraw, Image  

image = Image.open("HEALTH_CARD.png")  

draw = ImageDraw.Draw(image)  

font = ImageFont.truetype("arial.ttf", 15)  

draw.text((10, 250), "Name: Rajkumar Ahire", font=font, fill='#000000')  
draw.text((10, 280), "Adress: Nasik Maharashtra", font=font, fill='#000000')  
draw.text((10, 310), "Date of Birth: 13/10/1999", font=font, fill='#000000')  
draw.text((10, 340), "Mobile: 7758017733", font=font, fill='#000000')  
draw.text((10, 370), "Email: rajkumarahire1310@gmail.com", font=font, fill='#000000')  
draw.text((10, 400), "Health Insurance Number : 1234567890", font=font, fill='#000000')  
draw.text((10, 430), "Adhar Card number : 111111111111", font=font, fill='#000000')  
draw.text((10, 480), "", font=font, fill='#000000')  

image = image.convert('RGB')
image.save('report.pdf')
