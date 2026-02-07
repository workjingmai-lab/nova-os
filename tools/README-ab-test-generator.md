# A/B Test Generator

Generate message variants for A/B testing outreach campaigns.

## Usage

```bash
python3 tools/ab-test-generator.py <message_file>
```

## Example

```bash
python3 tools/ab-test-generator.py outreach/messages/001-charlinho-services.md
```

## Output

Creates 3 variant files:
- `*-variantA.md` — Original (control)
- `*-variantB.md` — Tweaked hook/subject  
- `*-variantC.md` — Different angle/framing

## Variants Generated

| Variant | Strategy | Use Case |
|---------|----------|----------|
| A | Original message | Control/baseline |
| B | Value-first subject + personalization | Higher open rate test |
| C | Question-based + problem-first opening | Different angle test |

## Workflow

1. Create base message with research
2. Generate variants with this tool
3. Customize each variant
4. Send 5-10 of each to test
5. Track reply rates
6. Scale winning variant
