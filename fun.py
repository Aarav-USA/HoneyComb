import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

client = commands.Bot(command_prefix="hc!",intents=discord.Intents.all())

@client.event
async def on_ready():
    print('The bot is ready!')

@client.command()
async def avatar(ctx, member: discord.Member=None): 
  if member is None:
    member=ctx.author
  favatar=discord.Embed(title=f"{member.name}'s Avatar",color = discord.Colour.gold())
  favatar.set_footer(text=f"Requested by: {ctx.author.name}")

  favatar.set_image(url='{}'.format(member.avatar_url))
  await ctx.send(embed=favatar)
@client.command()
async def dadjoke(ctx):
    await ctx.send(random.choice(mylist))

mylist = ["Imagine if you walked into a bar and there was a long line of people waiting to take a swing at you. That's the punch line.", "Why is it a bad idea to iron your four-leaf clover? Cause you shouldn't press your luck.", 
"I ordered a chicken and an egg from Amazon. I'll let you know.", "I can't take my dog to the pond anymore because the ducks keep attacking him. That's what I get for buying a pure bread dog.", 
"My wife said I was immature. So I told her to get out of my fort.", "I didn't want to believe that my dad was stealing from his job as a traffic cop, but when I got home, all the signs were there.", 
"I spent a lot of time, money, and effort childproofing my house… but the kids still get in.", "What rock group has four men that don't sing? Mount Rushmore.", "When I was a kid, my mother told me I could be anyone I wanted to be. Turns out, identity theft is a crime.", 
"A guy goes to his doctor because he can see into the future. The doctor asks him, How long have you suffered from that condition? The guy tells him, Since next Monday.", "What do sprinters eat before a race? Nothing, they fast!", 
"What concert costs just 45 cents? 50 Cent featuring Nickelback!", "What do you call a mac 'n' cheese that gets all up in your face? Too close for comfort food!", "Why couldn't the bicycle stand up by itself? It was two tired!",
"Did you hear about the restaurant on the moon? Great food, no atmosphere!", "Why do melons have weddings? Because they cantaloupe!", "What happens when you go to the bathroom in France? European.", 
"What's the difference between a poorly dressed man on a tricycle and a well-dressed man on a bicycle? Attire!", "How many apples grow on a tree? All of them!", "Did you hear the rumor about butter? Well, I'm not going to spread it!", 
"Did you hear about the guy who invented Lifesavers?  They say he made a mint!", "Last night I had a dream that I weighed less than a thousandth of a gram. I was like, 0mg.", "A cheese factory exploded in France. Da brie is everywhere!", 
"Why did the old man fall in the well? Because he couldn't see that well!", "What do you call a factory that sells passable products? A satisfactory!", "Why did the invisible man turn down the job offer? He couldn't see himself doing it!", 
"Want to hear a joke about construction? I'm still working on it!", "I was really angry at my friend Mark for stealing my dictionary. I told him, Mark, my words!", "How does Moses make his coffee? Hebrews it.", 
"I'm starting a new dating service in Prague. It's called Czech-Mate.", "I was just reminiscing about the beautiful herb garden I had when I was growing up. Good thymes.", "Do you know the last thing my grandfather said to me before he kicked the bucket? Grandson, watch how far I can kick this bucket.", 
"Why do dogs float in water? Because they are good buoys.", "What kind of music did the pilgrims listen to? Plymouth rock.", "What kind of music did the pilgrims listen to? Plymouth rock.", "What is the tallest building in the world? The library—it's got the most stories.", 
"What do you call a beehive without an exit? Unbelievable.", "I like telling Dad jokes. Sometimes he laughs!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "What do you call a fish with two knees? A two-knee fish!", 
"Why do you never see elephants hiding in trees? Because they're so good at it!", "How does a penguin build its house? Igloos it together!", "Why don't skeletons ever go trick or treating? Because they have no body to go with!", 
"This graveyard looks overcrowded. People must be dying to get in there!", "What's ET short for? Because he's only got tiny legs!", "What's brown and sticky? A stick!", "Can February march? No, but April may!", 
"What's orange and sounds like a parrot? A carrot!", "How do you make a Kleenex dance? Put some boogie in it!", "Why is Peter Pan always flying? He neverlands!", "What's a ninja's favorite type of shoes? Sneakers!", "What do Santa's elves listen to ask they work? Wrap music!", 
"Did you hear about the bacon cheeseburger who couldn't stop telling jokes? It was on a roll.", "Why was the coach yelling at a vending machine? He wanted his quarter back.", "Why do vampires seem sick? They're always coffin.", 
"I used to run a dating service for chickens. But I was struggling to make hens meet.", "I wish Covid-19 had started in Las Vegas. Because what happens in Vegas stays in Vegas.", "Why couldn't the green pepper practice archery? Because it didn't habanero.", 
"Why did the stadium get so hot after the game? Because all the fans left.", "What do you call a sad cup of coffee? Depresso.", "After an unsuccessful harvest, why did the farmer decide to try a career in music? Because he had a ton of sick beets.", 
"My dog used to chase people on a scooter a lot. It got so bad we had to take his scooter away.", "Within minutes, the detectives knew what the murder weapon was. It was a brief case.", "Not to brag but I made six figures last year. I was also named worst employee at the toy factory.", 
"To whoever stole my copy of Microsoft Office, I will find you. You have my Word!", "I used to work in a shoe-recycling shop. It was sole destroying!", "My boss told me to have a good day, so I went home!", "I'm so good at sleeping I can do it with my eyes closed!", 
"Spring is here! I got so excited I wet my plants!", "I thought about going on an all-almond diet… But that's just nuts!", "My friend says to me, What rhymes with orange? And I told him, No it doesn't!", "My wife told me I had to stop acting like a flamingo. So I had to put my foot down!", 
"I told my girlfriend she drew her eyebrows too high. She seemed surprised!", "I tell dad jokes but I have no kids…I'm a faux pa!", "So a vowel saves another vowel's life. The other vowel says, Aye E! I owe you!", "Did I tell you the time I fell in love during a backflip? I was heels over head!", 
"My uncle named his dogs Rolex and Timex. They're his watch dogs!", "If you see a robbery at an Apple Store does that make you an iWitness?!", "I would avoid the sushi if I were you. It's a little fishy!", "Five out of four people admit they're bad with fractions!", 
"Two goldfish are in a tank. One says to the other, Do you know how to drive this thing?", "I'll call you later. Don't call me later, call me Dad!", "Did you hear about the Italian chef who died? He pasta way!", "When the grocery store clerk asks me if I want the milk in a bag, I always tell him, No, I'd rather drink it out of the carton!", 
"The difference between a numerator and a denominator is a short line. Only a fraction of people will understand this!", "I don't play soccer because I enjoy the sport. I'm just doing it for kicks!", "I invented a new word today: Plagiarism!", "What do you call a donkey with only three legs? A wonkey!", 
"After dinner, my wife asked if I could clear the table. I needed a running start, but I made it!", "This morning, Siri said, Don't call me Shirley. I accidentally left my phone in Airplane mode!", "A woman is on trial for beating her husband to death with his guitar collection. The judge asks her, First offender? She says, No, first a Gibson! Then a Fender!", 
"I know a lot of jokes about retired people but none of them work!", "What do you call a guy with a rubber toe? Roberto!", "What rhymes with boo and stinks? You!", "I accidentally dropped my pillow on the floor. I think it has a concushion.",
"Someone complimented my parking today! They left a sweet note on my windshield that said parking fine.", "St. Francis worked at Krispy Kreme. He was a deep friar.", "In America, using the metric system can get you in legal trouble. In fact, if you sneer at any other method of measuring liquids, you may be held in contempt of quart.", 
"I found a wooden shoe in my toilet today. It was clogged.", "Some people can't distinguish between etymology and entomology. They bug me in ways I, can't put into words.", "My hotel tried to charge me ten dollars extra for air conditioning. That wasn't cool.", 
"I hate it when people say age is only a number. Age is clearly a word.", "Have you heard about those new corduroy pillows? They're making headlines", "An apple a day keeps the doctor away. At least it does if you throw it hard enough", "I asked my date to meet me at the gym but she never showed up. I guess the two of us aren't going to work out.", 
"A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas. These are the pie rates of the Caribbean.", "My friend was showing me his tool shed and pointed to a ladder. That's my stepladder, he said. I never knew my real ladder.", "Did you hear about the ATM that got addicted to money? It suffered from withdrawals.", 
"I'm reading a horror story in braille. Something bad is going to happen, I can just feel it.", "My doctor told me I was going deaf. The news was hard for me to hear.", "Which days are the strongest? Saturday and Sunday. The rest are weekdays.", "If an English teacher is convicted of a crime and doesn't complete the sentence, is that a fragment?"
"I think my wife is putting glue on my antique weapons collection. She denies it but I'm sticking to my guns!", "Which U.S. state is famous for its extra-small soft drinks? Minnesota!", "I got a hen to regularly count her own eggs. She's a real mathamachicken!", 
"What did the Ranch say when someone opened the refrigerator door? Close the door, I'm dressing!", "Why do trees seem suspicious on sunny days? They just seem a little shady!", "What did the policeman say to his belly button? You're under a vest!", "What do you call a fake noodle? An Impasta!", 
"I've been bored recently so I've decided to take up fencing. The neighbors said they will call the police unless I put it back.", "Why did the math book look so sad? Because of all of its problems!", "I don't really call for funerals that start before noon. I guess I'm just not a mourning person!", 
"If two vegans get in a fight, is it still considered a beef?", "One of my favorite memories as a kid was when my brothers used to put me inside a tire and roll me down a hill. They were Goodyears!", "I'm addicted to collecting vintage Beatles albums. I need Help!", 
"What does the cell say to his sister when she steps on his toe? Oh my toe sis!", "I never buy pre-shredded cheese. Because doing it yourself is grate.", "I was playing chess with my friend and he said, Let's make this interesting. So we stopped playing chess.", "How do you tell the difference between a bull and a milk cow? It is either one or the utter.", 
"I have a great joke about nepotism. But I'll only tell it to my kids.", "What do scholars eat when they're hungry? Academia nuts.", "What do you call an ant that has been shunned by his community? A socially dissed ant.", "A Vicks VapoRub truck overturned on the highway this morning. Amazingly, there was no congestion for eight hours!", "When does a joke become a dad joke? When it becomes apparent.", 
"I'm afraid for the calendar. Its days are numbered.", "My wife said I should do lunges to stay in shape. That would be a big step forward.", "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!", "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.", "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.", 
"What do you call a fish wearing a bowtie? Sofishticated.", "How do you follow Will Smith in the snow?" "You follow the fresh prints.", "If April showers bring May flowers, what do May flowers bring? Pilgrims.", "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.", 
"What do you call a factory that makes okay products?" "A satisfactory.", "Dear Math, grow up and solve your own problems.", "What did the janitor say when he jumped out of the closet?" "Supplies!", "Have you heard about the chocolate record player? It sounds pretty sweet.", "What did the ocean say to the beach? Nothing, it just waved."]

client.run("ODMwMzEwNjIwMDU0MjkwNDcz.YHE1Bg.2Q-1Rnz6pfbvJkyCcQigAuBeiCY")
