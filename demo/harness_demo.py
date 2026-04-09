TEST_CASES = [
    {"input": "系统崩了，客户现在无法付款", "expected": "high"},
    {"input": "接口报错，已经影响线上用户", "expected": "high"},
    {"input": "请问发票什么时候开", "expected": "medium"},
    {"input": "麻烦帮我查一下订单状态", "expected": "medium"},
    {"input": "谢谢，已经解决了", "expected": "low"},
    {"input": "先不用了，我自己再看看", "expected": "low"},
]


def classify_priority(text: str) -> str:
    text = text.lower()

    if "崩" in text or "无法付款" in text or "报错" in text or "线上" in text:
        return "high"

    if "发票" in text or "订单" in text or "查一下" in text:
        return "medium"

    return "low"


def evaluate_case(case: dict) -> dict:
    prediction = classify_priority(case["input"])
    passed = prediction == case["expected"]

    return {
        "input": case["input"],
        "expected": case["expected"],
        "prediction": prediction,
        "passed": passed,
    }


def run_harness(test_cases: list[dict]) -> None:
    results = [evaluate_case(case) for case in test_cases]
    passed_count = sum(item["passed"] for item in results)
    total = len(results)
    accuracy = passed_count / total if total else 0

    print("=" * 60)
    print("Harness 测试结果")
    print("=" * 60)
    print(f"总用例数: {total}")
    print(f"通过数: {passed_count}")
    print(f"通过率: {accuracy:.2%}")
    print()

    print("失败用例明细：")
    failed = [item for item in results if not item["passed"]]

    if not failed:
        print("- 无，全部通过")
        return

    for item in failed:
        print(f"- 输入: {item['input']}")
        print(f"  期望: {item['expected']}")
        print(f"  预测: {item['prediction']}")
        print()


if __name__ == "__main__":
    run_harness(TEST_CASES)
