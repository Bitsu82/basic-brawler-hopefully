import pygame,sys
import basic_brawler as bb
from basic_brawler import State

pygame.init()

#making the screen
HIEGHT = 800
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HIEGHT))
clock = pygame.time.Clock()

    #setting up player character 

all_sprites = pygame.sprite.Group()
guy1 = bb.PlayerCharacter("Arthur", "guy.jpg", 100, 400, all_sprites, scale = 0.25)
guy2 = bb.PlayerCharacter("Merlin", "guy2.jpeg", 1000, 400, all_sprites, scale = 0.505)
    




while True:   
    keys = pygame.key.get_pressed()

    #guy1 controls

    if keys[pygame.K_a] and guy1.state == State.IDLE:
        guy1.rect.x -= 3
        guy1.facing = 'left'
    if keys[pygame.K_d] and guy1.state == State.IDLE:
        guy1.rect.x += 3
        guy1.facing = 'right'
        #guy 2 controls
    if keys[pygame.K_LEFT] and guy2.state == State.IDLE:
        guy2.rect.x -= 3
        guy2.facing = 'left'
    if keys[pygame.K_RIGHT] and guy2.state == State.IDLE:
        guy2.rect.x += 3
        guy2.facing = 'right'


    for event in pygame.event.get():
        if event.type == pygame.K_UP:
            guy2.jump
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("For months we have been suffering under the torture of a problem which the Versailles Diktat created - a problem which has deteriorated until it becomes intolerable for us. Danzig was and is a German city. The Corridor was and is German. Both these territories owe their cultural development exclusively to the German people. Danzig was separated from us, the Corridor was annexed by Poland. As in other German territories of the East, all German minorities living there have been ill-treated in the most distressing manner. More than 1,000,000 people of German blood had in the years 1919-1920 to leave their homeland. As always, I attempted to bring about, by the peaceful method of making proposals for revision, an alteration of this intolerable position. It is a lie when the outside world says that we only tried to carry through our revisions by pressure. Fifteen years before the National Socialist Party came to power there was the opportunity of carrying out these revisions by peaceful settlements and understanding. On my own initiative I have, not once but several times, made proposals for the revision of intolerable conditions. All these proposals, as you know, have been rejected - proposals for limitation of armaments and even, if necessary, disarmament, proposals for limitation of warmaking, proposals for the elimination of certain methods of modern warfare. You know the proposals that I have made to fulfill the necessity of restoring German sovereignty over German territories. You know the endless attempts I made for a peaceful clarification and understanding of the problem of Austria, and later of the problem of the Sudetenland, Bohemia, and Moravia. It was all in vain. It is impossible to demand that an impossible position should be cleared up by peaceful revision and at the same time constantly reject peaceful revision. It is also impossible to say that he who undertakes to carry out these revisions for himself transgresses a law, since the Versailles Diktat is not law to us. A signature was forced out of us with pistols at our head and with the threat of hunger for millions of people. And then this document, with our signature, obtained by force, was proclaimed as a solemn law. In the same way, I have also tried to solve the problem of Danzig, the Corridor, etc., by proposing a peaceful discussion. That the problems had to be solved was clear. It is quite understandable to us that the time when the problem was to be solved had little interest for the Western Powers. But that time is not a matter of indifference to us. Moreover, it was not and could not be a matter of indifference to those who suffer most. In my talks with Polish statesmen I discussed the ideas which you recognize from my last speech to the Reichstag. No one could say that this was in any way an inadmissible procedure on undue pressure. I then naturally formulated at last the German proposals, and I must once more repeat that there is nothing more modest or loyal than these proposals. I should like to say this to the world. I alone was in the position to make such proposal, for I know very well that in doing so I brought myself into opposition to millions of Germans. These proposals have been refused. Not only were they answered first with mobilization, but with increased terror and pressure against our German compatriots and with a slow strangling of the Free City of Danzig - economically, politically, and in recent weeks by military and transport means. Poland has directed its attacks against the Free City of Danzig. Moreover, Poland was not prepared to settle the Corridor question in a reasonable way which would be equitable to both parties, and she did not think of keeping her obligations to minorities. I must here state something definitely; German has kept these obligations; the minorities who live in Germany are not persecuted. No Frenchman can stand up and say that any Frenchman living in the Saar territory is oppressed, tortured, or deprived of his rights. Nobody can say this. For four months I have calmly watched developments, although I never ceased to give warnings. In the last few days I have increased these warnings. I informed the Polish Ambassador three weeks ago that if Poland continued to send to Danzig notes in the form of ultimata, and if on the Polish side an end was not put to Customs measures destined to ruin Danzig's trade, then the Reich could not remain inactive. I left no doubt that people who wanted to compare the Germany of to-day with the former Germany would be deceiving themselves. An attempt was made to justify the oppression of the Germans by claiming that they had committed acts of provocation. I do not know in what these provocations on the part of women and children consist, if they themselves are maltreated, in some cases killed. One thing I do know - that no great Power can with honour long stand by passively and watch such events. I made one more final effort to accept a proposal for mediation on the part of the British Government. They proposed, not that they themselves should carry on the negotiations, but rather that Poland and Germany should come into direct contact and once more pursue negotiations. I must declare that I accepted this proposal, and I worked out a basis for these negotiations which are known to you. For two whole days I sat in my Government and waited to see whether it was convenient for the Polish Government to send a plenipotentiary or not. Last night they did not send us a plenipotentiary, but instead informed us through their Ambassador that they were still considering whether and to what extent they were in a position to go into the British proposals. The Polish Government also said that they would inform Britain of their decision. Deputies, if the German Government and its Leader patiently endured such treatment Germany would deserve only to disappear from the political stage. But I am wrongly judged if my love of peace and my patience are mistaken for weakness or even cowardice. I, therefore, decided last night and informed the British Government that in these circumstances I can no longer find any willingness on the part of the Polish Government to conduct serious negotiations with us. These proposals for mediation have failed because in the meanwhile there, first of all, came as an answer the sudden Polish general mobilization, followed by more Polish atrocities. These were again repeated last night. Recently in one night there were as many as twenty-one frontier incidents: last night there were fourteen, of which three were quite serious. I have, therefore, resolved to speak to Poland in the same language that Poland for months past has used toward us. This attitude on the part of the Reich will not change. The other European States understand in part our attitude. I should like here above all to thank Italy, which throughout has supported us, but you will understand that for the carrying on of this struggle we do not intend to appeal to foreign help. We will carry out this task ourselves. The neutral States have assured us of their neutrality, just as we had already guaranteed it to them. When statesmen in the West declare that this affects their interests, I can only regret such a declaration. It cannot for a moment make me hesitate to fulfill my duty. What more is wanted? I have solemnly assured them, and I repeat it, that we ask nothing of those Western States and never will ask anything. I have declared that the frontier between France and Germany is a final one. I have repeatedly offered friendship and, if necessary, the closest co-operation to Britain, but this cannot be offered from one side only. It must find response on the other side. Germany has no interests in the West, and our western wall is for all time the frontier of the Reich on the west. Moreover, we have no aims of any kind there for the future. With this assurance we are in solemn earnest, and as long as others do not violate their neutrality we will likewise take every care to respect it. I am happy particularly to be able to tell you of one event. You know that Russia and Germany are governed by two different doctrines. There was only one question that had to be cleared up. Germany has no intention of exporting its doctrine. Given the fact that Soviet Russia has no intention of exporting its doctrine to Germany. I no longer see any reason why we should still oppose one another. On both sides we are clear on that. Any struggle between our people would only be of advantage to others. We have, therefore, resolved to conclude a pact which rules out for ever any use of violence between us. It imposes the obligation on us to consult together in certain European questions. It makes possible for us economic co-operation, and above all it assures that the powers of both these powerful States are not wasted against one another. Every attempt of the West to bring about any change in this will fail. At the same time I should like here to declare that this political decision means a tremendous departure for the future, and that it is a final one. Russia and Germany fought against one another in the World War. That shall and will not happen a second time. In Moscow, too, this pact was greeted exactly as you greet it. I can only endorse word for word the speech of Russian Foreign Commissar, Molotov. I am determined to solve (1) the Danzig question; (2) the question of the Corridor; and (3) to see to it that a change is made in the relationship between Germany and Poland that shall ensure a peaceful co-existence. In this I am resolved to continue to fight until either the present Polish government is willing to continue to bring about this change or until another Polish Government is ready to do so. I am resolved t remove from the German frontiers the element of uncertainty, the everlasting atmosphere of conditions resembling civil war. I will see to it that in the East there is, on the frontier, a peace precisely similar to that on our other frontiers. In this I will take the necessary measures to se that they do not contradict the proposals I have already made known in the Reichstag itself to the rest of the world, that is to say, I will not war against women and children. I have ordered my air force to restrict itself to attacks on military objectives. If, however, the enemy thinks he can form that draw carte blanche on his side to fight by the other methods he will receive an answer that will deprive him of hearing and sight. This night for the first time Polish regular soldiers fired on our territory. Since 5.45 A.M. we have been returning the fire, and from now on bombs will be met by bombs. Whoever fight with poison gas will be fought with poison gas. Whoever departs from the rules of humane warfare can only expect that we shall do the same. I will continue this struggle, no matter against whom, until the safety of the Reich and its rights are secured. For six years now I have been working on the building up of the German defenses. Over 90 millions have in that time been spent on the building up of these defense forces. They are now the best equipped and are above all comparison with what they were in 1914. My trust in them is unshakable. When I called up these forces and when I now ask sacrifices of the German people and if necessary every sacrifice, then I have a right to do so, for I also am to-day absolutely ready, just as we were formerly, to make every possible sacrifice. I am asking of no German man more than I myself was ready throughout four years at any time to do. There will be no hardships for Germans to which I myself will not submit. My whole life henceforth belongs more than ever to my people. I am from now on just first soldier of the German Reich. I have once more put on that coat that was the most sacred and dear to me. I will not take it off again until victory is secured, or I will not survive the outcome. Should anything happen to me in the struggle then my first successor is Party Comrade Goring; should anything happen to Party Comrade Goring my next successor is Party Comrade Hess. You would then be under obligation to give to them as Fuhrer the same blind loyalty and obedience as to myself. Should anything happen to Party Comrade Hess, then by law the Senate will be called, and will choose from its midst the most worthy - that is to say the bravest - successor. As a National Socialist and as German soldier I enter upon this struggle with a stout heart. My whole life has been nothing but one long struggle for my people, for its restoration, and for Germany. There was only one watchword for that struggle: faith in this people. One word I have never learned: that is, surrender. If, however, anyone thinks that we are facing a hard time, I should ask him to remember that once a Prussian King, with a ridiculously small State, opposed a stronger coalition, and in three wars finally came out successful because that State had that stout heart that we need in these times. I would, therefore, like to assure all the world that a November 1918 will never be repeated in German history. Just as I myself am ready at any time to stake my life - anyone can take it for my people and for Germany - so I ask the same of all others. Whoever, however, thinks he can oppose this national command, whether directly of indirectly, shall fall. We have nothing to do with traitors. We are all faithful to our old principle. It is quite unimportant whether we ourselves live, but it is essential that our people shall live, that Germany shall live. The sacrifice that is demanded of us is not greater than the sacrifice that many generations have made. If we form a community closely bound together by vows, ready for anything, resolved never to surrender, then our will will master every hardship and difficulty. And I would like to close with the declaration that I once made when I began the struggle for power in the Reich. I then said: If our will is so strong that no hardship and suffering can subdue it, then our will and our German might shall prevail.")
                pygame.quit()
                sys.exit()
            if event.key  == pygame.K_w and guy1.state == State.IDLE:
                guy1.jump()
            if event.key  ==  pygame.K_UP and guy2.state == State.IDLE:
                guy2.jump()
            if event.key == pygame.K_e and guy1.state == State.IDLE:
                guy1.punch(guy2)
            if event.key == pygame.K_m and guy1.state == State.IDLE:
                guy2.punch(guy1)
            if event.key == pygame.K_f and guy1.state == State.IDLE:
                guy1.use_shield()
            if event.key == pygame.K_SPACE and guy2.state == State.IDLE:
                guy2.use_shield()
    




    all_sprites.update()
    screen.fill((0, 30, 30))
    all_sprites.draw(screen)
    if guy1.punch_hitbox:
        pygame.draw.rect(screen, (255, 0, 0), guy1.punch_hitbox, 2)
    if guy2.punch_hitbox:
        pygame.draw.rect(screen, (255, 255, 0), guy2.punch_hitbox, 2)
    if guy1.shield_hitbox:
        pygame.draw.rect(screen, (255, 0, 0), guy1.shield_hitbox,2)
    if guy2.shield_hitbox:
        pygame.draw.rect(screen, (255, 255, 0), guy2.shield_hitbox, 2)

    pygame.display.update()
    clock.tick(60)
            
