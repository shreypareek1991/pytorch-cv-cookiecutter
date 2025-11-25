#!/usr/bin/env bash
set -euo pipefail

# Trivy vulnerability scanner for Docker images
# Usage: ./scan.sh [--image IMAGE_NAME] [--severity CRITICAL,HIGH] [--format table|json]

IMAGE="{{ cookiecutter.docker_image_name }}"
SEVERITY="CRITICAL,HIGH"
FORMAT="table"
FAIL_ON="CRITICAL"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --image)
      IMAGE="$2"
      shift 2
      ;;
    --severity)
      SEVERITY="$2"
      shift 2
      ;;
    --format)
      FORMAT="$2"
      shift 2
      ;;
    --fail-on)
      FAIL_ON="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: $0 [--image IMAGE] [--severity SEVERITIES] [--format FORMAT] [--fail-on SEVERITY]"
      exit 1
      ;;
  esac
done

# Check if trivy is installed
if ! command -v trivy &> /dev/null; then
    echo "❌ Trivy is not installed."
    echo "Install it with:"
    echo "  brew install trivy  # macOS"
    echo "  or visit: https://aquasecurity.github.io/trivy/latest/getting-started/installation/"
    exit 1
fi

echo "🔍 Scanning Docker image: ${IMAGE}"
echo "   Severity filter: ${SEVERITY}"
echo "   Format: ${FORMAT}"
echo ""

# Run Trivy scan
if trivy image \
    --severity "${SEVERITY}" \
    --format "${FORMAT}" \
    --exit-code 0 \
    "${IMAGE}"; then
    echo ""
    echo "✅ Scan completed successfully"
    
    # Check for critical vulnerabilities if fail-on is set
    if [[ -n "${FAIL_ON}" ]]; then
        echo "🔍 Checking for ${FAIL_ON} vulnerabilities..."
        if trivy image \
            --severity "${FAIL_ON}" \
            --format table \
            --exit-code 1 \
            --quiet \
            "${IMAGE}" 2>/dev/null; then
            echo "❌ Found ${FAIL_ON} vulnerabilities. Build may fail in CI/CD."
            exit 1
        else
            echo "✅ No ${FAIL_ON} vulnerabilities found"
        fi
    fi
else
    echo ""
    echo "⚠️  Scan found vulnerabilities (see above)"
    exit 1
fi

