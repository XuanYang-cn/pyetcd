unittest:
	PYTHONPATH=`pwd` python3 -m pytest tests --cov=pyetcd -v

lint:
	PYTHONPATH=`pwd` pylint --rcfile=pylint.conf pyetcd

codecov:
	PYTHONPATH=`pwd` pytest --cov=pyetcd --cov-report=xml tests -x -v -rxXs

package:
	python3 -m build --sdist --wheel --outdir dist/ .

gen_proto:
	./python_gen.sh
