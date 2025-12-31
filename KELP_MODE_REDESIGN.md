# Mzansi Kelp Quest - Complete Redesign Implementation Guide

## Overview
The kelp mode needs a complete redesign based on the new specification. This document outlines all the changes needed.

## Key Systems to Implement

### 1. Bait System
- Players start with 0 bait
- Mzansi Buoy station (x: 100, y: 100) - Answer CAPS MCQ to earn 1 bait (correct answer)
- Wrong answer = learning modal
- Bait required to cast (1 bait per cast)

### 2. Fishing System
- Cast requires 1 bait
- Cast near water (SPACE/click)
- Hook random fish by zone/rod level
- Question on hook (CAPS MCQ based on fish rarity/difficulty)
- Correct = add to inventory, Wrong = escape + review

### 3. Fish Inventory System
- Backpack capacity (4/8/20 based on upgrade)
- Fish stored with rarity, name, MZN value
- Cannot catch if inventory full

### 4. Harbour Market
- Station at (700, 500)
- Sell all fish in inventory for MZN
- Cash In power: 1.3x multiplier

### 5. Areas & Zones
- Cape Kelp Base (free, commons)
- Purple Kelp Pond (MZN10, uncommons)
- Sandy Shores Reef (MZN85, rares)
- Cosmic Cove (MZN250, epics/legendaries)
- Lucky Lagoon (MZN1000, one-time, mysterious/mythic)
- Boat Launch station (50, 550) to buy tickets

### 6. Fish Rarities
- Common (MZN1-2)
- Uncommon (MZN5)
- Rare (MZN10-20)
- Epic (MZN40-65)
- Legendary (MZN100)
- Mysterious (MZN150, requires berry)
- Mythic (MZN5000, requires special berry)

### 7. Berries
- Collectibles in world
- Blackberry, Redberry, Blueberry, Goldenberry
- Required for mysterious/mythic fish

### 8. Upgrades
- Backpacks: Small (4, free), Medium (8, MZN20), Large (20, MZN60)
- Rods: Basic (free), Expert (MZN75, +15% rare chance)
- Powers: Bolt (MZN30, speed), No Wait (MZN40, instant cast), Cash In (MZN70, 1.3x sell)

### 9. Modern Features
- AR Fish Viewer (interactive catch modal)
- Daily Quests (localStorage)
- Activity Feed (player achievements)
- Photo Mode (canvas.toDataURL + clipboard)

### 10. Weather System
- Calm/Storm states
- Storms slow boat movement

## Implementation Priority

1. **Core Systems** (Must Have):
   - Bait system + Mzansi Buoy
   - Fishing with bait requirement
   - Fish inventory
   - Harbour Market
   - Basic areas (base + 1-2 others)

2. **Secondary Systems** (Should Have):
   - All areas + tickets
   - Berries system
   - All upgrades

3. **Polish Features** (Nice to Have):
   - AR viewer
   - Daily quests
   - Activity feed
   - Photo mode

## File Changes Required

1. Replace kelpSketch function (lines ~5657-6143)
2. Replace startKelpMode function (already done)
3. Update all kelp helper functions
4. Add new UI modals (Buoy, Market, Boat Launch, Shops)
5. Update kelp stats display to show bait count
6. Add activity feed UI element























