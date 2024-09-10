python run.py \
  --model_name gpt4-turbo \
  --repo_path ~/Documents/SWE-agent-example1 \
  --data_path ~/Documents/SWE-agent-example1/issues/auto_qa.md \
  --config_file config/auto_qa.yaml \
  --per_instance_cost_limit 2.00 \
  --apply_patch_locally
