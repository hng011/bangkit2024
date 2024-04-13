FROM datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_3.4.16-20220815

RUN python3 -m pip install --upgrade pip

RUN apt-get install -y \
	build-essential \
	cmake \
	git \
	unzip \
	pkg-config \
	libopenblas-dev \
	liblapack-dev \
	libhdf5-dev \
	graphviz \
	&& apt-get clean \
	$$ rm -rf /var/lib/apt/lists/*

RUN apt-get install -y \
	python3-numpy \
	python3-scipy \
	python3-matplotlib \
	python3-yaml \
	python3-h5py \
	python3-opencv \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install seaborn pandas notebook pyarrow scikit-learn pydot-ng theano
