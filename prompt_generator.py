
from random import choice

prompt_objects = ["airplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "dining table", "dog", "horse", "motorbike", "person", "potted plant", "sheep", "sofa", "train", "tv monitor"]
prompt_environments = ["out in nature", "indoors", "in the city", "at an office"]
prompt_lighting = ["well-lit", "dimly lit", "with some fog or smoke"]
prompt_styles = ["photorealistic", "HD", "professional photography", "amateur photography", "CCTV footage quality", "dashcam view", "drone view"]

def prompt_gen(n: int = 500) -> List[str]:
    """Creates a list of prompts for generating"""
    prompts = []
    for _ in range(n):
        p = f"{choice(prompt_styles)} photo of a {choice(prompt_objects)} and a {choice(prompt_objects)} {choice(prompt_environments)}, {choice(prompt_lighting)}"
        prompts.append(p)
    return prompts



"""

Other ideas


1. Environments (Background & Context)
Focus: Clutter, texture confusion, and complex geometries that act as "Hard Negatives."

"Inside a chaotic warehouse with cardboard boxes piled high" (Tests occlusion and similar textures)

"On a wet asphalt street reflecting city neon signs" (Tests reflections and ground-plane confusion)

"In a dense forest with dappled sunlight filtering through leaves" (Tests high-frequency noise and camouflage)

"Crowded subway platform during rush hour" (Tests heavy occlusion and crowd density)

"Construction site filled with scaffolding and orange safety netting" (Tests grid-like occlusions)

"Minimalist white cleanroom laboratory" (Tests objects against sterile, low-texture backgrounds)

"Rusty industrial scrapyard with piles of metal debris" (Tests texture confusion with metal objects)

"Grocery store aisle with fully stocked colorful shelves" (Tests "clutter" distraction)

"Snow-covered parking lot with tire tracks" (Tests low contrast white-on-white)

"Inside a dimly lit parking garage with concrete pillars" (Tests low light and structural occlusion)

"Dusty desert road with heat haze shimmering" (Tests atmospheric distortion)

"Cluttered home office desk with tangled cables and papers" (Tests small object context)

"Foggy harbor dock with shipping containers" (Tests atmospheric visual obstruction)

"Overgrown backyard with tall grass and weeds" (Tests bottom-up occlusion)

"Reflective glass building facade reflecting the sky" (Tests mirror images/false positives)

"Inside a moving subway car with motion outside windows" (Tests dynamic backgrounds)

"Muddy off-road trail with puddles" (Tests dirty/obscured ground planes)

"Nighttime festival with confetti and hanging lights" (Tests airborne visual noise)

"Hospital corridor with linoleum floors and harsh overhead lights" (Tests sterile, high-glare environments)

"Post-disaster rubble with broken concrete and rebar" (Tests irregular geometry backgrounds)

2. Lighting Conditions
Focus: dynamic range, shadows, and color temperature shifts.

"Harsh midday sun casting long, sharp shadows" (Tests shadow confusion)

"Soft, diffused overcast lighting with low contrast" (Tests flat texture definition)

"Backlit by a setting sun, creating a silhouette effect" (Tests shape recognition without internal detail)

"Illuminated by flickering fluorescent strip lights" (Tests color banding and green tint)

"Pitch black darkness with only a flashlight beam illuminating the center" (Tests extreme spotlighting)

"Golden hour sunlight with heavy lens flare" (Tests optical artifacts washing out the image)

"Neon blue and pink cyberpunk street lighting" (Tests extreme color domain shift)

"Volumetric fog with light shafts piercing through" (Tests contrast reduction via atmosphere)

"Under streetlamps with sodium-vapor orange glow" (Tests monochromatic color shift)

"Strobe lighting effects freezing motion" (Tests unnatural sharpness/highlights)

"High-contrast Chiaroscuro lighting" (Tests extreme black/white transition)

"Reflected light from a nearby swimming pool (caustics)" (Tests moving light patterns)

"Overexposed and washed out (high-key)" (Tests loss of highlight detail)

"Underexposed and grainy (low-key)" (Tests sensor noise in shadows)

"Dappled shade under a tree" (Tests uneven illumination on the object)

"Lit by the glow of a computer screen in a dark room" (Tests cool, weak directional light)

"Flash photography with harsh frontal lighting" (Tests flattening of 3D features)

"Twilight 'blue hour' ambient light" (Tests low color contrast)

"Light filtering through rain streaks on a window" (Tests lighting combined with foreground obstruction)

"Infrared night vision style (monochrome green/grey)" (Tests specific sensor modalities)

3. Styles (Sensor & Camera Artifacts)
Focus: Instead of "artistic" styles, focus on "imaging" styles to mimic camera defects.

"Viewed through a fisheye security camera lens (CCTV)" (Tests barrel distortion)

"Low-resolution webcam footage with compression artifacts" (Tests JPEG blocking and blur)

"Motion blurred action shot" (Tests loss of edge definition)

"Shot on a vintage polaroid with color fading" (Tests color degradation)

"Drone aerial top-down view" (Tests extreme angle change)

"GoPro wide-angle footage from a helmet mount" (Tests perspective distortion)

"Telephoto zoom lens compressing the background" (Tests loss of depth cues)

"Macro close-up with shallow depth of field (bokeh)" (Tests out-of-focus context)

"Grainy ISO 3200 night photography" (Tests high-frequency sensor noise)

"Dashcam footage with windshield glare" (Tests viewing through glass)

"Thermal imaging heatmap style" (Tests non-RGB domain adaptation)

"Glitch art style with digital transmission errors" (Tests robustness to data corruption)

"Smartphone photo with over-sharpening filters applied" (Tests edge ringing artifacts)

"Vignetted image with dark corners" (Tests lens quality issues)

"Chromatic aberration (color fringing) on edges" (Tests lens misalignment artifacts)

"Water droplets on the camera lens blurring parts of the image" (Tests lens obstruction)

"Scanline artifacts from an old CRT monitor" (Tests legacy video formats)

"Double exposure ghosting effect" (Tests motion ghosting)

"Dutch angle (tilted camera)" (Tests rotational invariance)

"Fogged up camera lens" (Tests low contrast/blur)

Next Step
Would you like to move to Phase 3 (Auto-Labeling) and see a more detailed breakdown of how to set up the "Zero-Shot" detector?"""

""" Generation data
[1/1] prompt='CCTV footage quality photo of a bottle and a bicycle at an office, dimly lit' steps=6 guidance=0.0 seed=283899293173206638 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-1.png
[2/1] prompt='professional photography photo of a chair and a cat out in nature, well-lit' steps=6 guidance=0.0 seed=7857340850679316712 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-2.png
[3/1] prompt='professional photography photo of a person and a person in the city, well-lit' steps=6 guidance=0.0 seed=62458887655371533 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-3.png
[4/1] prompt='drone view photo of a motorbike and a horse in the city, dimly lit' steps=6 guidance=0.0 seed=2065885465004139702 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-4.png
[5/1] prompt='photorealistic photo of a dog and a tv monitor indoors, dimly lit' steps=6 guidance=0.0 seed=5019684140994758789 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-5.png
[6/1] prompt='photorealistic photo of a train and a dog indoors, dimly lit' steps=6 guidance=0.0 seed=7877170002704583952 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-6.png
[7/1] prompt='CCTV footage quality photo of a person and a motorbike out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=5228885324135828283 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-7.png
[8/1] prompt='drone view photo of a boat and a person indoors, with some fog or smoke' steps=6 guidance=0.0 seed=1981594937582170221 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-8.png
[9/1] prompt='CCTV footage quality photo of a cat and a car in the city, well-lit' steps=6 guidance=0.0 seed=610585333679100239 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-9.png
[10/1] prompt='professional photography photo of a cat and a tv monitor out in nature, dimly lit' steps=6 guidance=0.0 seed=8326197166856660664 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-10.png
[11/1] prompt='dashcam view photo of a potted plant and a cow indoors, with some fog or smoke' steps=6 guidance=0.0 seed=2416122014433446792 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-11.png
[12/1] prompt='professional photography photo of a cat and a bicycle in the city, well-lit' steps=6 guidance=0.0 seed=5621724954708408177 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-12.png
[13/1] prompt='HD photo of a chair and a dining table indoors, dimly lit' steps=6 guidance=0.0 seed=1331632461202884344 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-13.png
[14/1] prompt='photorealistic photo of a airplane and a sofa in the city, well-lit' steps=6 guidance=0.0 seed=7250628704270038952 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-14.png
[15/1] prompt='photorealistic photo of a sofa and a horse at an office, dimly lit' steps=6 guidance=0.0 seed=6172407182416070013 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-15.png
[16/1] prompt='photorealistic photo of a motorbike and a bottle in the city, dimly lit' steps=6 guidance=0.0 seed=5660628349648175982 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-16.png
[17/1] prompt='dashcam view photo of a airplane and a dog out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=392418254577027090 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-17.png
[18/1] prompt='CCTV footage quality photo of a dining table and a bicycle at an office, with some fog or smoke' steps=6 guidance=0.0 seed=2378958271140391882 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-18.png
[19/1] prompt='professional photography photo of a sofa and a train out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=8762114751575584524 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-19.png
[20/1] prompt='HD photo of a car and a dining table indoors, with some fog or smoke' steps=6 guidance=0.0 seed=726282121487225132 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-20.png
[21/1] prompt='CCTV footage quality photo of a dining table and a dog indoors, with some fog or smoke' steps=6 guidance=0.0 seed=7936368110168026033 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-21.png
[22/1] prompt='professional photography photo of a car and a potted plant indoors, well-lit' steps=6 guidance=0.0 seed=1401585466811618613 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-22.png
[23/1] prompt='drone view photo of a person and a chair at an office, dimly lit' steps=6 guidance=0.0 seed=4593100726774776210 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-23.png
[24/1] prompt='dashcam view photo of a sheep and a sheep out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=5762633762912177368 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-24.png
[25/1] prompt='photorealistic photo of a chair and a car at an office, with some fog or smoke' steps=6 guidance=0.0 seed=5248770478863040895 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-25.png
[26/1] prompt='photorealistic photo of a car and a sheep in the city, with some fog or smoke' steps=6 guidance=0.0 seed=4168305501503886446 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-26.png
[27/1] prompt='drone view photo of a bottle and a chair indoors, well-lit' steps=6 guidance=0.0 seed=2514303825826750392 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-27.png
[28/1] prompt='CCTV footage quality photo of a boat and a bus out in nature, well-lit' steps=6 guidance=0.0 seed=502723830459698359 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-28.png
[29/1] prompt='CCTV footage quality photo of a bird and a car out in nature, well-lit' steps=6 guidance=0.0 seed=7798482261220255384 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-29.png
[30/1] prompt='dashcam view photo of a dining table and a sheep at an office, with some fog or smoke' steps=6 guidance=0.0 seed=6023489813573880547 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-30.png
[31/1] prompt='professional photography photo of a chair and a bicycle at an office, well-lit' steps=6 guidance=0.0 seed=341693260164720354 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-31.png
[32/1] prompt='drone view photo of a boat and a boat in the city, well-lit' steps=6 guidance=0.0 seed=2709124239722713384 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-32.png
[33/1] prompt='drone view photo of a bird and a cow out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=9190290566151952497 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-33.png
[34/1] prompt='dashcam view photo of a car and a car in the city, well-lit' steps=6 guidance=0.0 seed=9055617516723550913 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-34.png
[35/1] prompt='drone view photo of a potted plant and a person at an office, with some fog or smoke' steps=6 guidance=0.0 seed=2309667669551051096 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-35.png
[36/1] prompt='photorealistic photo of a person and a cat in the city, dimly lit' steps=6 guidance=0.0 seed=1152125464547267772 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-36.png
[37/1] prompt='photorealistic photo of a sofa and a bottle out in nature, well-lit' steps=6 guidance=0.0 seed=6938835061138279176 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-37.png
[38/1] prompt='HD photo of a dining table and a bicycle indoors, with some fog or smoke' steps=6 guidance=0.0 seed=4840182751582953739 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-38.png
[39/1] prompt='drone view photo of a cat and a airplane out in nature, dimly lit' steps=6 guidance=0.0 seed=6355775183043911062 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-39.png
[40/1] prompt='drone view photo of a dog and a tv monitor in the city, dimly lit' steps=6 guidance=0.0 seed=9080337052264065972 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-40.png
[41/1] prompt='HD photo of a horse and a motorbike out in nature, dimly lit' steps=6 guidance=0.0 seed=8154319725750029316 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-41.png
[42/1] prompt='photorealistic photo of a horse and a bus in the city, dimly lit' steps=6 guidance=0.0 seed=6543973593898010911 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-42.png
[43/1] prompt='amateur photography photo of a motorbike and a chair out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=7812078422104161069 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-43.png
[44/1] prompt='photorealistic photo of a bird and a cat in the city, dimly lit' steps=6 guidance=0.0 seed=2459591730263952546 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-44.png
[45/1] prompt='CCTV footage quality photo of a potted plant and a car in the city, with some fog or smoke' steps=6 guidance=0.0 seed=9162185387193629653 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-45.png
[46/1] prompt='CCTV footage quality photo of a sheep and a tv monitor indoors, dimly lit' steps=6 guidance=0.0 seed=1356964532378029197 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-46.png
[47/1] prompt='dashcam view photo of a chair and a sofa indoors, with some fog or smoke' steps=6 guidance=0.0 seed=6728676184867039069 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-47.png
[48/1] prompt='photorealistic photo of a chair and a motorbike in the city, with some fog or smoke' steps=6 guidance=0.0 seed=7330865955398246320 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-48.png
[49/1] prompt='HD photo of a bus and a bicycle in the city, with some fog or smoke' steps=6 guidance=0.0 seed=4636555107314150662 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-49.png
[50/1] prompt='CCTV footage quality photo of a motorbike and a tv monitor in the city, well-lit' steps=6 guidance=0.0 seed=7367332957133773791 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-50.png
[51/1] prompt='professional photography photo of a bus and a bicycle at an office, with some fog or smoke' steps=6 guidance=0.0 seed=5328190797827005283 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-51.png
[52/1] prompt='dashcam view photo of a car and a horse indoors, with some fog or smoke' steps=6 guidance=0.0 seed=4717349141182177703 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-52.png
[53/1] prompt='HD photo of a motorbike and a dining table at an office, with some fog or smoke' steps=6 guidance=0.0 seed=4997208344036201485 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-53.png
[54/1] prompt='dashcam view photo of a dog and a motorbike in the city, well-lit' steps=6 guidance=0.0 seed=1123224302576139043 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-54.png
[55/1] prompt='amateur photography photo of a dog and a airplane indoors, with some fog or smoke' steps=6 guidance=0.0 seed=5137058029046477668 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-55.png
[56/1] prompt='professional photography photo of a cat and a dining table indoors, with some fog or smoke' steps=6 guidance=0.0 seed=6277041646381217374 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-56.png
[57/1] prompt='amateur photography photo of a sofa and a dining table at an office, well-lit' steps=6 guidance=0.0 seed=3240441818711873228 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-57.png
[58/1] prompt='CCTV footage quality photo of a horse and a sheep in the city, well-lit' steps=6 guidance=0.0 seed=6859413246366890538 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-58.png
[59/1] prompt='professional photography photo of a tv monitor and a potted plant indoors, dimly lit' steps=6 guidance=0.0 seed=6504414023023732124 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-59.png
[60/1] prompt='photorealistic photo of a potted plant and a boat at an office, well-lit' steps=6 guidance=0.0 seed=1823916551164135796 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-60.png
[61/1] prompt='CCTV footage quality photo of a boat and a bus out in nature, well-lit' steps=6 guidance=0.0 seed=9218426272880146514 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-61.png
[62/1] prompt='photorealistic photo of a dining table and a cat at an office, with some fog or smoke' steps=6 guidance=0.0 seed=260705835010380664 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-62.png
[63/1] prompt='dashcam view photo of a potted plant and a tv monitor at an office, with some fog or smoke' steps=6 guidance=0.0 seed=1162781334698068420 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-63.png
[64/1] prompt='dashcam view photo of a sheep and a bicycle indoors, dimly lit' steps=6 guidance=0.0 seed=4091191321750461556 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-64.png
[65/1] prompt='drone view photo of a motorbike and a cow out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=8782978159719390234 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-65.png
[66/1] prompt='amateur photography photo of a cow and a horse out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=9122565451190951291 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-66.png
[67/1] prompt='dashcam view photo of a bottle and a boat indoors, well-lit' steps=6 guidance=0.0 seed=7284966264559439083 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-67.png
[68/1] prompt='professional photography photo of a potted plant and a tv monitor at an office, well-lit' steps=6 guidance=0.0 seed=2243837371039331259 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-68.png
[69/1] prompt='dashcam view photo of a bird and a sofa at an office, dimly lit' steps=6 guidance=0.0 seed=1980799933186857797 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-69.png
[70/1] prompt='HD photo of a bird and a car out in nature, dimly lit' steps=6 guidance=0.0 seed=433074978219720975 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-70.png
[71/1] prompt='HD photo of a horse and a sofa in the city, dimly lit' steps=6 guidance=0.0 seed=1370785339689472580 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-71.png
[72/1] prompt='HD photo of a chair and a train out in nature, dimly lit' steps=6 guidance=0.0 seed=398602823319144464 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-72.png
[73/1] prompt='dashcam view photo of a train and a tv monitor in the city, with some fog or smoke' steps=6 guidance=0.0 seed=8764943606009703719 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-73.png
[74/1] prompt='CCTV footage quality photo of a airplane and a motorbike at an office, with some fog or smoke' steps=6 guidance=0.0 seed=1724056717752365057 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-74.png
[75/1] prompt='HD photo of a chair and a person at an office, well-lit' steps=6 guidance=0.0 seed=7702747918880827029 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-75.png
[76/1] prompt='dashcam view photo of a cow and a car at an office, dimly lit' steps=6 guidance=0.0 seed=3379880187153266796 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-76.png
[77/1] prompt='dashcam view photo of a dining table and a sofa indoors, with some fog or smoke' steps=6 guidance=0.0 seed=577718252138509281 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-77.png
[78/1] prompt='CCTV footage quality photo of a cow and a car at an office, well-lit' steps=6 guidance=0.0 seed=7969643336529687252 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-78.png
[79/1] prompt='professional photography photo of a chair and a motorbike at an office, well-lit' steps=6 guidance=0.0 seed=4598557403719920196 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-79.png
[80/1] prompt='professional photography photo of a bus and a dog in the city, well-lit' steps=6 guidance=0.0 seed=4692979849604968832 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-80.png
[81/1] prompt='photorealistic photo of a car and a sofa at an office, well-lit' steps=6 guidance=0.0 seed=3986162049640712158 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-81.png
[82/1] prompt='professional photography photo of a cow and a potted plant indoors, dimly lit' steps=6 guidance=0.0 seed=8514893309097648412 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-82.png
[83/1] prompt='drone view photo of a dining table and a sofa out in nature, well-lit' steps=6 guidance=0.0 seed=4420555386937420597 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-83.png
[84/1] prompt='HD photo of a dining table and a cat in the city, well-lit' steps=6 guidance=0.0 seed=2362702236176727946 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-84.png
[85/1] prompt='drone view photo of a bird and a tv monitor out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=1035731599108211669 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-85.png
[86/1] prompt='CCTV footage quality photo of a train and a car indoors, with some fog or smoke' steps=6 guidance=0.0 seed=5041500461090564402 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-86.png
[87/1] prompt='amateur photography photo of a cat and a bottle out in nature, well-lit' steps=6 guidance=0.0 seed=7947385117456420753 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-87.png
[88/1] prompt='amateur photography photo of a tv monitor and a car out in nature, well-lit' steps=6 guidance=0.0 seed=5674636394036855837 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-88.png
[89/1] prompt='drone view photo of a sofa and a car in the city, dimly lit' steps=6 guidance=0.0 seed=191791860713708309 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-89.png
[90/1] prompt='amateur photography photo of a chair and a airplane indoors, with some fog or smoke' steps=6 guidance=0.0 seed=5270665205352616745 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-90.png
[91/1] prompt='amateur photography photo of a airplane and a horse indoors, dimly lit' steps=6 guidance=0.0 seed=8389103685909204328 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-91.png
[92/1] prompt='professional photography photo of a person and a horse indoors, dimly lit' steps=6 guidance=0.0 seed=2618265311283161625 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-92.png
[93/1] prompt='amateur photography photo of a tv monitor and a cat at an office, with some fog or smoke' steps=6 guidance=0.0 seed=5566522591088107866 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-93.png
[94/1] prompt='CCTV footage quality photo of a train and a cat out in nature, well-lit' steps=6 guidance=0.0 seed=2764116008670457785 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-94.png
[95/1] prompt='drone view photo of a train and a dog indoors, well-lit' steps=6 guidance=0.0 seed=6993810503654106903 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-95.png
[96/1] prompt='dashcam view photo of a person and a cow in the city, with some fog or smoke' steps=6 guidance=0.0 seed=7899381814787971877 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-96.png
[97/1] prompt='dashcam view photo of a bottle and a car indoors, with some fog or smoke' steps=6 guidance=0.0 seed=806432764206420971 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-97.png
[98/1] prompt='amateur photography photo of a potted plant and a horse out in nature, dimly lit' steps=6 guidance=0.0 seed=5297974583808917519 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-98.png
[99/1] prompt='amateur photography photo of a sofa and a sofa at an office, well-lit' steps=6 guidance=0.0 seed=7268698597500819615 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-99.png
[100/1] prompt='drone view photo of a cow and a motorbike at an office, with some fog or smoke' steps=6 guidance=0.0 seed=1292470868097379763 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-100.png
[101/1] prompt='CCTV footage quality photo of a dining table and a car indoors, dimly lit' steps=6 guidance=0.0 seed=2313150758054528339 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-101.png
[102/1] prompt='professional photography photo of a cow and a dining table indoors, well-lit' steps=6 guidance=0.0 seed=7035504324100193530 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-102.png
[103/1] prompt='professional photography photo of a chair and a potted plant indoors, well-lit' steps=6 guidance=0.0 seed=268636295491172189 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-103.png
[104/1] prompt='drone view photo of a chair and a motorbike indoors, with some fog or smoke' steps=6 guidance=0.0 seed=323618020968215207 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-104.png
[105/1] prompt='CCTV footage quality photo of a bird and a car in the city, dimly lit' steps=6 guidance=0.0 seed=6468980197097046858 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-105.png
[106/1] prompt='photorealistic photo of a bird and a dog out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=3643918169231905214 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-106.png
[107/1] prompt='dashcam view photo of a tv monitor and a airplane indoors, dimly lit' steps=6 guidance=0.0 seed=6985933236230515690 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-107.png
[108/1] prompt='HD photo of a car and a boat at an office, dimly lit' steps=6 guidance=0.0 seed=4172516485447052006 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-108.png
[109/1] prompt='drone view photo of a dog and a chair out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=1323519484002055770 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-109.png
[110/1] prompt='amateur photography photo of a chair and a sheep at an office, with some fog or smoke' steps=6 guidance=0.0 seed=576295424325794642 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-110.png
[111/1] prompt='professional photography photo of a bicycle and a chair out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=4817181405839387973 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-111.png
[112/1] prompt='professional photography photo of a tv monitor and a tv monitor at an office, with some fog or smoke' steps=6 guidance=0.0 seed=6638884053382415371 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-112.png
[113/1] prompt='professional photography photo of a bicycle and a tv monitor in the city, dimly lit' steps=6 guidance=0.0 seed=3969211767858028772 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-113.png
[114/1] prompt='drone view photo of a sofa and a cat indoors, with some fog or smoke' steps=6 guidance=0.0 seed=8371126668725180484 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-114.png
[115/1] prompt='professional photography photo of a bicycle and a boat in the city, well-lit' steps=6 guidance=0.0 seed=7529308241662127612 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-115.png
[116/1] prompt='photorealistic photo of a dog and a motorbike in the city, well-lit' steps=6 guidance=0.0 seed=104993167445509292 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-116.png
[117/1] prompt='amateur photography photo of a bottle and a potted plant at an office, well-lit' steps=6 guidance=0.0 seed=3507353607773387610 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-117.png
[118/1] prompt='drone view photo of a cat and a cat at an office, dimly lit' steps=6 guidance=0.0 seed=2998030355213721625 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-118.png
[119/1] prompt='drone view photo of a dining table and a tv monitor indoors, well-lit' steps=6 guidance=0.0 seed=860125792129985983 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-119.png
[120/1] prompt='drone view photo of a sofa and a airplane indoors, with some fog or smoke' steps=6 guidance=0.0 seed=781357409789487345 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-120.png
[121/1] prompt='photorealistic photo of a bottle and a dining table out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=9177668010695891371 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-121.png
[122/1] prompt='photorealistic photo of a cat and a horse at an office, well-lit' steps=6 guidance=0.0 seed=3916097441485172321 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-122.png
[123/1] prompt='amateur photography photo of a motorbike and a dog at an office, with some fog or smoke' steps=6 guidance=0.0 seed=6403167024599129908 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-123.png
[124/1] prompt='CCTV footage quality photo of a dog and a dog in the city, with some fog or smoke' steps=6 guidance=0.0 seed=7946855815567970800 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-124.png
[125/1] prompt='drone view photo of a person and a train at an office, dimly lit' steps=6 guidance=0.0 seed=1616601435167588838 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-125.png
[126/1] prompt='amateur photography photo of a motorbike and a tv monitor out in nature, dimly lit' steps=6 guidance=0.0 seed=6879000328856367178 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-126.png
[127/1] prompt='professional photography photo of a sheep and a bicycle at an office, well-lit' steps=6 guidance=0.0 seed=2900517217662153660 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-127.png
[128/1] prompt='amateur photography photo of a dog and a chair out in nature, well-lit' steps=6 guidance=0.0 seed=1927324447546991178 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-128.png
[129/1] prompt='photorealistic photo of a person and a boat out in nature, dimly lit' steps=6 guidance=0.0 seed=2660553999057743674 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-129.png
[130/1] prompt='CCTV footage quality photo of a train and a motorbike indoors, with some fog or smoke' steps=6 guidance=0.0 seed=4927625461937517307 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-130.png
[131/1] prompt='photorealistic photo of a airplane and a sofa in the city, with some fog or smoke' steps=6 guidance=0.0 seed=7932670225519052378 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-131.png
[132/1] prompt='professional photography photo of a bus and a car out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=173047910450550100 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-132.png
[133/1] prompt='HD photo of a chair and a bird indoors, with some fog or smoke' steps=6 guidance=0.0 seed=3235649713219515835 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-133.png
[134/1] prompt='CCTV footage quality photo of a bus and a boat indoors, well-lit' steps=6 guidance=0.0 seed=8118043994648304785 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-134.png
[135/1] prompt='dashcam view photo of a bottle and a bus in the city, well-lit' steps=6 guidance=0.0 seed=814758745422449972 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-135.png
[136/1] prompt='dashcam view photo of a tv monitor and a cow out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=7887146739679540683 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-136.png
[137/1] prompt='HD photo of a dining table and a chair indoors, well-lit' steps=6 guidance=0.0 seed=8933404677917822434 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-137.png
[138/1] prompt='photorealistic photo of a cat and a chair at an office, well-lit' steps=6 guidance=0.0 seed=4128156078826850172 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-138.png
[139/1] prompt='dashcam view photo of a horse and a bus in the city, dimly lit' steps=6 guidance=0.0 seed=8806017255398909897 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-139.png
[140/1] prompt='professional photography photo of a bottle and a boat in the city, well-lit' steps=6 guidance=0.0 seed=6974675902778800929 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-140.png
[141/1] prompt='dashcam view photo of a sofa and a car out in nature, well-lit' steps=6 guidance=0.0 seed=8737543554980417474 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-141.png
[142/1] prompt='HD photo of a dining table and a airplane in the city, with some fog or smoke' steps=6 guidance=0.0 seed=6226923823587436773 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-142.png
[143/1] prompt='dashcam view photo of a bicycle and a bottle in the city, with some fog or smoke' steps=6 guidance=0.0 seed=5789842619065722989 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-143.png
[144/1] prompt='dashcam view photo of a cat and a airplane at an office, dimly lit' steps=6 guidance=0.0 seed=2610010599817945638 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-144.png
[145/1] prompt='HD photo of a cat and a car out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=1132476248436898676 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-145.png
[146/1] prompt='CCTV footage quality photo of a train and a bus at an office, dimly lit' steps=6 guidance=0.0 seed=3812582374729797478 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-146.png
[147/1] prompt='CCTV footage quality photo of a boat and a motorbike in the city, well-lit' steps=6 guidance=0.0 seed=8175771063503914064 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-147.png
[148/1] prompt='amateur photography photo of a bird and a bus indoors, well-lit' steps=6 guidance=0.0 seed=6082586688376619995 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-148.png
[149/1] prompt='CCTV footage quality photo of a person and a bottle in the city, dimly lit' steps=6 guidance=0.0 seed=8716935260418699722 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-149.png
[150/1] prompt='photorealistic photo of a bus and a airplane indoors, with some fog or smoke' steps=6 guidance=0.0 seed=3686172213131658691 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-150.png
[151/1] prompt='dashcam view photo of a person and a motorbike indoors, with some fog or smoke' steps=6 guidance=0.0 seed=1803421756408016168 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-151.png
[152/1] prompt='professional photography photo of a dog and a bus indoors, dimly lit' steps=6 guidance=0.0 seed=1982592972203066420 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-152.png
[153/1] prompt='dashcam view photo of a airplane and a car indoors, dimly lit' steps=6 guidance=0.0 seed=7816189558919943290 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-153.png
[154/1] prompt='dashcam view photo of a motorbike and a bicycle at an office, dimly lit' steps=6 guidance=0.0 seed=4597530862333204324 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-154.png
[155/1] prompt='CCTV footage quality photo of a bicycle and a bicycle indoors, dimly lit' steps=6 guidance=0.0 seed=1450454738444025301 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-155.png
[156/1] prompt='HD photo of a horse and a bicycle in the city, well-lit' steps=6 guidance=0.0 seed=1245530671863502031 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-156.png
[157/1] prompt='drone view photo of a tv monitor and a person in the city, dimly lit' steps=6 guidance=0.0 seed=1919335254740786075 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-157.png
[158/1] prompt='dashcam view photo of a bird and a horse indoors, well-lit' steps=6 guidance=0.0 seed=6448382272582982516 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-158.png
[159/1] prompt='HD photo of a chair and a horse in the city, with some fog or smoke' steps=6 guidance=0.0 seed=3982063262731155742 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-159.png
[160/1] prompt='CCTV footage quality photo of a dining table and a car at an office, with some fog or smoke' steps=6 guidance=0.0 seed=4631465053164743412 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-160.png
[161/1] prompt='drone view photo of a car and a train out in nature, dimly lit' steps=6 guidance=0.0 seed=3984244824765350698 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-161.png
[162/1] prompt='amateur photography photo of a sheep and a bicycle indoors, dimly lit' steps=6 guidance=0.0 seed=1879055803124309336 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-162.png
[163/1] prompt='professional photography photo of a sofa and a dining table at an office, dimly lit' steps=6 guidance=0.0 seed=2620483055901006047 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-163.png
[164/1] prompt='CCTV footage quality photo of a cat and a dining table at an office, well-lit' steps=6 guidance=0.0 seed=6450226805133124685 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-164.png
[165/1] prompt='photorealistic photo of a bus and a bottle at an office, dimly lit' steps=6 guidance=0.0 seed=7138020225356616897 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-165.png
[166/1] prompt='drone view photo of a boat and a boat at an office, dimly lit' steps=6 guidance=0.0 seed=2270882721368007525 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-166.png
[167/1] prompt='photorealistic photo of a person and a sheep out in nature, dimly lit' steps=6 guidance=0.0 seed=3297339171169889810 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-167.png
[168/1] prompt='amateur photography photo of a cow and a bottle out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=5933646931535086567 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-168.png
[169/1] prompt='amateur photography photo of a motorbike and a dog at an office, dimly lit' steps=6 guidance=0.0 seed=6326074376205660512 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-169.png
[170/1] prompt='professional photography photo of a potted plant and a bird in the city, dimly lit' steps=6 guidance=0.0 seed=2677960267728672726 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-170.png
[171/1] prompt='amateur photography photo of a bird and a bicycle indoors, well-lit' steps=6 guidance=0.0 seed=7735502263111237508 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-171.png
[172/1] prompt='dashcam view photo of a chair and a cow indoors, dimly lit' steps=6 guidance=0.0 seed=5569747383435838695 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-172.png
[173/1] prompt='drone view photo of a bird and a bus out in nature, dimly lit' steps=6 guidance=0.0 seed=2313810496626253591 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-173.png
[174/1] prompt='HD photo of a cat and a dog out in nature, well-lit' steps=6 guidance=0.0 seed=3599841552435740813 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-174.png
[175/1] prompt='amateur photography photo of a cat and a car in the city, with some fog or smoke' steps=6 guidance=0.0 seed=3729952954324580580 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-175.png
[176/1] prompt='amateur photography photo of a sheep and a tv monitor at an office, dimly lit' steps=6 guidance=0.0 seed=4623660661462115684 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-176.png
[177/1] prompt='photorealistic photo of a sheep and a tv monitor indoors, dimly lit' steps=6 guidance=0.0 seed=35462454177911569 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-177.png
[178/1] prompt='photorealistic photo of a sheep and a bus out in nature, well-lit' steps=6 guidance=0.0 seed=4255588991348395675 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-178.png
[179/1] prompt='professional photography photo of a train and a dog out in nature, dimly lit' steps=6 guidance=0.0 seed=762803294864798215 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-179.png
[180/1] prompt='dashcam view photo of a sheep and a sheep at an office, well-lit' steps=6 guidance=0.0 seed=3665292389371279795 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-180.png
[181/1] prompt='dashcam view photo of a car and a potted plant indoors, with some fog or smoke' steps=6 guidance=0.0 seed=206820790802590272 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-181.png
[182/1] prompt='amateur photography photo of a dog and a cow out in nature, well-lit' steps=6 guidance=0.0 seed=1409185190399349836 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-182.png
[183/1] prompt='HD photo of a boat and a bird indoors, well-lit' steps=6 guidance=0.0 seed=2582801269605788541 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-183.png
[184/1] prompt='dashcam view photo of a boat and a sheep in the city, with some fog or smoke' steps=6 guidance=0.0 seed=223232976891906433 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-184.png
[185/1] prompt='amateur photography photo of a sofa and a dog out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=2294763832030763899 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-185.png
[186/1] prompt='professional photography photo of a sheep and a bird out in nature, well-lit' steps=6 guidance=0.0 seed=6805734397710053282 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-186.png
[187/1] prompt='professional photography photo of a dining table and a potted plant indoors, well-lit' steps=6 guidance=0.0 seed=2077611066847805386 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-187.png
[188/1] prompt='photorealistic photo of a cat and a train at an office, dimly lit' steps=6 guidance=0.0 seed=8709983819091451979 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-188.png
[189/1] prompt='photorealistic photo of a dog and a tv monitor in the city, dimly lit' steps=6 guidance=0.0 seed=7638901207567495525 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-189.png
[190/1] prompt='amateur photography photo of a potted plant and a train indoors, with some fog or smoke' steps=6 guidance=0.0 seed=1804914456400707993 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-190.png
[191/1] prompt='amateur photography photo of a train and a car indoors, well-lit' steps=6 guidance=0.0 seed=7676327300172577755 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-191.png
[192/1] prompt='photorealistic photo of a potted plant and a sheep out in nature, well-lit' steps=6 guidance=0.0 seed=1962996070680539189 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-192.png
[193/1] prompt='drone view photo of a potted plant and a cow at an office, well-lit' steps=6 guidance=0.0 seed=4427094703936475017 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-193.png
[194/1] prompt='photorealistic photo of a cat and a dining table out in nature, with some fog or smoke' steps=6 guidance=0.0 seed=6007905741585927613 size=416x416
Saved: /Users/atkwok/Projects/compvis/object_detection_cv/imagen/z-image-mps/output/test-night-194.png
[195/1] prompt='drone view photo of a chair and a potted plant in the city, well-lit' steps=6 guidance=0.0 seed=7889418815296400044 size=416x416
"""