FROM almalinux:9

RUN yum -y install epel-release
RUN yum -y install https://linux.davisnetworks.com/el9/updates/mrdvt92-release-8-3.el9.mrdvt92.noarch.rpm
RUN /usr/bin/crb enable
RUN yum -y update

# Change RPM here to the RPM that you are testing
RUN yum -y install perl-CPANPLUS #touch 3

# cat is the daemon here
CMD ["/usr/bin/cat"]
