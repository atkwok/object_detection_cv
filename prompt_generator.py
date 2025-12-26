import random

objects = ["airplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "dining table", "dog", "horse", "motorbike", "person", "potted plant", "sheep", "sofa", "train", "tv monitor"]
environments = ["out in nature", "indoors", "in the city", "at an office"]
lighting = ["well-lit", "dimly lit", "with some fog or smoke"]
styles = ["photorealistic", "HD", "professional photography", "amateur photography", "CCTV footage quality", "dashcam view", "drone view"]

def get_random_prompts(n=100):
    prompts = []
    for _ in range(n):
        p = f"A {random.choice(lighting)} photo of a {random.choice(objects)} in a {random.choice(environments)}, {random.choice(styles)}"
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