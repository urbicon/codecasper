import json
import os
import glob
import sys
from typing import List, Dict

def load_rule_file(file_path: str) -> Dict:
    """Loads a single rule file and checks for valid JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"\nERROR: Invalid JSON in file {file_path}")
        print(f"Details: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: Error reading file {file_path}")
        print(f"Details: {str(e)}")
        sys.exit(1)

def concatenate_rules():
    # Directory with rules
    rules_dir = "rules"
    # Output file
    output_rules = "Rules.json"
    
    # Check if rules directory exists
    if not os.path.exists(rules_dir):
        print(f"\nERROR: Directory '{rules_dir}' not found!")
        sys.exit(1)
    
    # Collect all rules
    all_rules: List[Dict] = []
    rule_files = glob.glob(os.path.join(rules_dir, "*.json"))
    
    if not rule_files:
        print(f"\nWARNING: No JSON files found in '{rules_dir}'!")
        sys.exit(1)
    
    for rule_file in rule_files:
        rule = load_rule_file(rule_file)
        all_rules.append(rule)
    
    # Sort rules by ruleId
    try:
        all_rules.sort(key=lambda x: x['ruleId'])
    except KeyError:
        print("\nERROR: At least one rule has no 'ruleId'!")
        sys.exit(1)
    
    # Write rules to output file
    try:
        with open(output_rules, 'w', encoding='utf-8') as f:
            json.dump(all_rules, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"\nERROR: Error writing output file {output_rules}")
        print(f"Details: {str(e)}")
        sys.exit(1)

    print(f"\nSuccessfully completed:")
    print(f"- Rules merged into {output_rules}")

if __name__ == "__main__":
    concatenate_rules()